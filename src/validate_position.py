def validate_position(function): 
    def validate_and_execute(position, *args, **kwargs): 
        if position < 0:
            raise ValueError("Position cannot be negative")

        return function(position, *args, **kwargs)

    return validate_and_execute
