import unittest
import numpy as np
from calculus import *

class TestIntegrationFunctions(unittest.TestCase):
    def test_simpson(self):
        # Test the Simpson's rule function
        def f(x):
            return x**2

        result = simpson(f, 0, 1, 100)
        self.assertAlmostEqual(result, 1/3, places=6)

    def test_trapezoid(self):
        # Test the trapezoidal rule function
        def f(x):
            return x**2

        result = trapezoid(f, 0, 1, 100)
        self.assertAlmostEqual(result, 1/3, places=6)

    def test_adaptive_trapezoid(self):
        # Test the adaptive trapezoidal rule function
        def f(x):
            return x**2

        result = adaptive_trapezoid(f, 0, 1, 0.0001, output=False)
        self.assertAlmostEqual(result, 1/3, places=6)

# Run the tests
test_suite = unittest.TestLoader().loadTestsFromTestCase(TestIntegrationFunctions)
unittest.TextTestRunner().run(test_suite)
