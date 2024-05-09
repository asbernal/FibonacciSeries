import unittest
from test_fibonacci_base import FibonacciBaseTest
from src.fibonacci_recursive import recursive_fibonacci

class FibonacciRecursiveTest(FibonacciBaseTest, unittest.TestCase):
    def get_fibonacci_function(self):
        return recursive_fibonacci


if __name__ == '__main__':
    unittest.main()
