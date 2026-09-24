# Rate Limiter
# Problem
# Allow only a fixed number of requests within a time window.
# Expected Output
# For a limit of 3 requests per 10 seconds:
# Request allowed
# Request allowed
# Request allowed
# Rate limit exceeded

from collections import deque
import time

class RateLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.request = deque()

    def allow(self):
        now = time.time()
        while self.request and now-self.request[0] >= self.window:
            self.request.popleft()
            if len(self.request) >= self.limit:
                return False
            self.request.append(now)
            return True
limiter = RateLimiter(3, 10)

for _ in range(4):
    if limiter.allow():
        print("Request allowed")
    else:
        print("Rate limit exceeded")