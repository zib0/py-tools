import time
from functools import wraps


def timer(func):

  @wraps(func)
  def wrapper(*args, **kwargs):
    start = time.perf_counter()

    # Call the actual function
    res = func(*args, **kwargs)

    duration = time.perf_counter() - start
    print(f'[{wrapper.__name__}] took {duration * 1000} ms')
    return res
  return wrapper