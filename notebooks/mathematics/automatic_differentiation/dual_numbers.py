from __future__ import annotations

import numpy as np
from typing import Callable

# definition of basic numeric type for convenience
NUMERIC = int | float

class Dual:
    def __init__(self, real: NUMERIC, dual: NUMERIC) -> None:
        self.real = real
        self.dual = dual

    @classmethod
    def coerce(cls, d: NUMERIC | "Dual") -> "Dual":
        # a real number is a dual number with zero dual part!
        return d if isinstance(d, Dual) else cls(d, 0)
    
    def __add__(self, other: NUMERIC | "Dual") -> "Dual":
        # (a + bε) + (c + dε) = (a + c) + (b + d)ε
        other = self.coerce(other)
        real = self.real + other.real
        dual = self.dual + other.dual
        return Dual(real, dual)

    def __radd__(self, other: NUMERIC | "Dual") -> "Dual":
        return self + other
    
    def __mul__(self, other: NUMERIC | "Dual") -> "Dual":
        # (a + bε) * (c + dε) = ac + (ad + bc)ε
        other = self.coerce(other)
        real = self.real * other.real
        dual = self.real * other.dual + self.dual * other.real
        return Dual(real, dual)

    def __rmul__(self, other: NUMERIC | "Dual") -> "Dual":
        return self * other

    def __sub__(self, other: NUMERIC | "Dual") -> "Dual":
        # subtraction is addition of the negative as per usual
        return self + (-1 * other)
    
    def __rsub__(self, other: NUMERIC | "Dual") -> "Dual":
        return other + (-1 * self)
    
    def __truediv__(self, other: NUMERIC | "Dual") -> "Dual":
        # since this is a bit more involved, we will set up the notation as in the note above
        other = self.coerce(other)
        a, b, c, d = self.real, self.dual, other.real, other.dual
        if c != 0:
            real = a / c
            dual = (b * c - a * d) / c / c
        else:
            if a == 0 and d != 0:
                real = b / d
                dual = 0
            else:
                raise ZeroDivisionError("Division by 'zero'!")
        return Dual(real, dual)
    
    def __rtruediv__(self, other: NUMERIC | "Dual") -> "Dual":
        other = self.coerce(other)
        return other / self
    
    def __pow__(self, other: NUMERIC | "Dual") -> "Dual":
        other = self.coerce(other)
        a, b, c, d = self.real, self.dual, other.real, other.dual
        # the only case where we'd allow a < 0 is if d = 0 and c is an integer
        if a < 0 and not (d == 0 and c.is_integer()):
            raise ValueError("Raising negative number to non-integer or dual power is undefined!")
        # we've handled the pathological case already, so safe to exponentiate and log here!
        if d == 0:
            real = a ** c
            dual = c * (a ** (c - 1)) * b
        else:
            real = a ** c
            dual = real * (b * c / a + d * np.log(a))
        return Dual(real, dual)
    
    def __rpow__(self, other: NUMERIC | "Dual") -> "Dual":
        other = self.coerce(other)
        return other ** self

    def __eq__(self, other: NUMERIC | "Dual") -> bool:
        # dual numbers are equal iff both their real and dual parts are equal
        other = self.coerce(other)
        return self.real == other.real and self.dual == other.dual
    
    def __repr__(self) -> str:
        return f"{self.real} + {self.dual}ε"


class FWAD:
    # we make the design choice to require the user to provide a function whose free parameters are resolved
    # prior to differentiation with respect to the target parameter
    # the alternative is handled by explicitly carrying the args and kwargs through
    @staticmethod
    def diff(func: Callable[[Dual], Dual]) -> Callable[[NUMERIC], NUMERIC]:
        def _diff(x: NUMERIC) -> NUMERIC:
            dual_x = Dual(x, 1)  # this is x + ε
            dual_result = func(dual_x)  # f(x + ε) = f(x) + f'(x)ε
            func_prime = dual_result.dual  # the dual part is the derivative at x!
            return func_prime
        return _diff


autodiff = FWAD()

# example: autodiff.diff(autodiff.diff(...(autodiff.diff(f))))(x) for nth order derivatives!
