import unittest
import time
from test_fibonacci_base import FibonacciBaseTest
from src.fibonacci_recursive import recursive_fibonacci
from src.fibonacci_memoized  import memoized_fibonacci

class FibonacciMemoizedTest(FibonacciBaseTest, unittest.TestCase): 
    def get_fibonacci_function(self):
        return memoized_fibonacci
    
    def measureCallTime(self, function, position):
        start = time.perf_counter()
        function(position)
        end = time.perf_counter()

        return end - start

    def test_performance_with_small_position(self): 
        recursive_time = self.measureCallTime(recursive_fibonacci, 5)
        memoized_time = self.measureCallTime(memoized_fibonacci, 5)

        self.assertTrue(recursive_time - memoized_time < 0.01) 

    def test_performance_with_large_position(self): 
        recursive_time = self.measureCallTime(recursive_fibonacci, 30)
        memoized_time = self.measureCallTime(memoized_fibonacci, 30)

        self.assertTrue(memoized_time * 10 < recursive_time) 

    
if __name__ == '__main__':
    unittest.main()
