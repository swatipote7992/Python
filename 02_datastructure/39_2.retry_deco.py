# Create a decorator that retries a function when it fails.

# Expected Output
# Attempt 1 failed
# Attempt 2 failed
# Success

from functools import wraps
import time


def retry_deco(max_attempt=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempt + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i} failed: {e}")
                    if i == max_attempt:
                        raise
                    time.sleep(2**i)

        return wrapper

    return decorator


@retry_deco(max_attempt=3)
def call_api():
    print("Calling API..")
    raise Exception("API unreachable")


call_api()