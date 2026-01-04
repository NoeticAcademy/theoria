import numpy as np
from dual_numbers import Dual, NUMERIC

# to use autodiff, we need to define a soft wrapper over numpy functions so that they handle dual numbers

class Dumpy:
    # we'll just do sine and exp for brevity. more can be added similarly
    @staticmethod
    def sin(x: NUMERIC | Dual) -> Dual:
        # sin(a + bε) = sin(a) + cos(a)bε
        x = Dual.coerce(x)
        real = np.sin(x.real)
        dual = np.cos(x.real) * x.dual
        return Dual(real, dual)

    @staticmethod
    def exp(x: NUMERIC | Dual) -> Dual:
        # exp(a + bε) = exp(a) + exp(a)bε
        x = Dual.coerce(x)
        real = np.exp(x.real)
        dual = real * x.dual
        return Dual(real, dual)

dp = Dumpy()
