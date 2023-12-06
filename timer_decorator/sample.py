import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        # Call the actual function
        res = func(*args, **kwargs)

        duration = time.perf_counter() - start
        print(f"[{wrapper.__name__}] took {duration * 1000} ms")
        return res

    return wrapper


@timer
def isprime(number: int):
    """Checks whether a number is a prime number"""
    isprime = False
    for i in range(2, number):
        if (number % i) == 0:
            isprime = True
            break
    return isprime


if __name__ == "__main__":
    isprime(number=155153)
