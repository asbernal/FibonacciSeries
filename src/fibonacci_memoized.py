from src.validate_position import validate_position
from src.fibonacci_recursive import recursive_fibonacci

@validate_position
def memoized_fibonacci(position, cache = None): 
    cache = {0: 1, 1: 1} if cache == None else cache

    if position not in cache:
        cache[position] = recursive_fibonacci(position, lambda _: memoized_fibonacci(_, cache))
    
    return cache[position]
