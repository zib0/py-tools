def repeater(iterations: int = 1):
    """Repeats the decorated function [iterations] times"""

    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            res = None
            for i in range(iterations):
                res = func(*args, **kwargs)
            return res

        return wrapper

    return outer_wrapper


@repeater(iterations=2)
def say_hello():
    print("hello")
