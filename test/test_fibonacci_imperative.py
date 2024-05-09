import unittest
from test_fibonacci_base import FibonacciBaseTest
from src.fibonacci_imperative import imperative_fibonacci

class FibonacciImperativeTest(FibonacciBaseTest, unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def get_fibonacci_function(self): 
        return imperative_fibonacci
    

if __name__ == '__main__':
    unittest.main()
