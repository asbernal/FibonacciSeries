import unittest
from parameterized import parameterized

class FibonacciBaseTest:    
    @parameterized.expand([ 
        (0, 1),
        (1, 1),
        (2, 2),
        (5, 8),
        (8, 34),
        (10, 89),
    ])
    def test_fibonacci(self, position, expected):
        self.assertEqual(self.get_fibonacci_function()(position), expected)
    
    def test_fibonacci_negative_position(self):
        self.assertRaises(ValueError, self.get_fibonacci_function(), -1)
        