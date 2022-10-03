import time
import tracemalloc
from functools import wraps


def performance_check(func):
    """Measure performance of a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
      tracemalloc.start()
      start_time = time.perf_counter()
      res = func(*args, **kwargs)
      duration = time.perf_counter() - start_time
      current, peak = tracemalloc.get_traced_memory()
      tracemalloc.stop()

      print(f"\nFunction:             {func.__name__} ({func.__doc__})"
            f"\nMemory usage:         {current / 10**6:.6f} MB"
            f"\nPeak memory usage:    {peak / 10**6:.6f} MB"
            f"\nDuration:             {duration:.6f} sec"
            f"\n{'-'*40}"
      )
      return res
    return wrapper

@performance_check
def isprime(number: int):
  """ Checks whether a number is a prime number """
  isprime = False
  for i in range(2, number):
    if ((number % i) == 0):
      isprime = True
      break
  return isprime

if __name__ == "__main__":
    a = isprime(number=155153)
    print(a)