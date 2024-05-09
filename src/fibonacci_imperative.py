from src.validate_position import validate_position

@validate_position
def imperative_fibonacci(position):
    previous, current = 1, 1 

    for i in range(2, position + 1):
        previous, current = current, previous + current
    
    return current
