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
        def wrapper(*args,**kwargs):
            for i in range(1, max_attempt+1):
                try:
                    func(*args, *kwargs)
                except Exception as e:
                    print(f"Attempt {i} failed")
                    if i == max_attempt:
                        raise
                    time.sleep(2 **(i-1))
            return wrapper
        return decorator
    return retry_deco


@retry_deco(max_attempt=3)
def call_api():
    print('Calling API..')
    return Exception