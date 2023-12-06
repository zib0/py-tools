import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        sec = end - start
        sec = sec % (24 * 3600)
        min = sec // 60
        hour = sec // 3600
        print(
            f"Execution time of {func.__name__}: {hour:.0f} hours, {min:.0f} minutes, {sec:.5f} seconds"
        )
        return result

    return wrapper