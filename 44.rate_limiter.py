# Rate Limiter
# Problem
# Allow only a fixed number of requests within a time window.
# Expected Output
# For a limit of 3 requests per 10 seconds:
# Request allowed
# Request allowed
# Request allowed
# Rate limit exceeded

from collections import defaultdict,deque
import time

class RateLimiter:
    def __init__(self, limit, window):
        self.limit = limit
        self.window = window
        self.requests = defaultdict(deque)

    def allow(self, req: str):
        now = time.time()
        timestamps = self.requests[req]
        while timestamps and timestamps[0] <= now - self.window:
            timestamps.popleft()
        if len(timestamps) >= self.limit:
            return False
        timestamps.append(now)
        return True

        
limiter = RateLimiter(3, 10)

for _ in range(4):
    if limiter.allow('newreq'):
        print("Request allowed")
    else:
        print("Rate limit exceeded")