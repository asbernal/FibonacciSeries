from src.validate_position import validate_position

@validate_position
def recursive_fibonacci(position,  function_to_call=lambda _  : recursive_fibonacci(_) ):

    return 1 if position < 2 else function_to_call(position - 1) + function_to_call(position - 2)
