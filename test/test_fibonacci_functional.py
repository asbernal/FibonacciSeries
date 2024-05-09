import unittest
from test_fibonacci_base import FibonacciBaseTest
from src.fibonacci_functional  import functional_fibonacci

class FibonacciFunctionalTest(FibonacciBaseTest, unittest.TestCase): 
    def get_fibonacci_function(self):
        return functional_fibonacci
        

if __name__ == '__main__':
    unittest.main()
    