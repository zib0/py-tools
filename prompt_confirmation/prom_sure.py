def prompt_sure(prompt_text: str):
    """Shows prompt asking you whether you want to continue. Exits on anything but y(es)"""

    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if input(prompt_text).lower() != "y":
                return
            return func(*args, **kwargs)

        return wrapper

    return outer_wrapper
