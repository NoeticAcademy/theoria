import logging
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

log = logging.getLogger("Validor")
log.setLevel(logging.INFO)
if not log.hasHandlers():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))
    log.addHandler(handler)


@dataclass
class TestCase:
    input_data: Dict[Any, Any]
    expected_output: Any
    description: Optional[str] = None


class Validor:
    """
    Simple testing (builder) framework for callables in notebooks.
    Users define TestCase instances and pass them to this tester.

    The reason not to use pytest directly:
    - Pytest relies on test discovery and filesystem structure, which is not ideal for notebooks.
    - Pytest and nbval can be cumbersome to set up for inline tests.
    """

    def __init__(self, func: Callable[..., Any]):
        self.func = func
        self._cases: List[TestCase] = []

    def add_case(self, case: TestCase) -> "Validor":
        self._cases.append(case)
        return self

    def add_cases(self, cases: List[TestCase]) -> "Validor":
        self._cases.extend(cases)
        return self

    @property
    def func_name(self) -> str:
        return self.func.__name__ if hasattr(self.func, "__name__") else str(self.func)

    def run(self, comparison: Callable[[Any, Any], bool] = lambda x, y: x == y) -> None:
        for i, case in enumerate(self._cases, 1):
            try:
                result = self.func(**case.input_data)
                log.info(f"Test {i} RUNNING: actual {result} vs expected {case.expected_output}")
                assert comparison(result, case.expected_output), (  # noqa: S101
                    f"Test {i} FAILED: {case.description}\n"
                    f"Input          : {case.input_data}\n"
                    f"Expected       : {case.expected_output}\n"
                    f"Got            : {result}"
                )
                log.debug(f"Test {i} PASSED: {case.description}")
            except AssertionError:
                raise
            except Exception as e:
                raise AssertionError(
                    f"Test {i} ERROR: {case.description}\n"
                    f"Input          : {case.input_data}\n"
                    f"Exception      : {e}"
                ) from e

        log.info(f"All {len(self._cases)} tests passed for {self.func_name}.")
