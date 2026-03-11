import time
from functools import wraps

def retry_with_backoff(max_attempts: int = 3, base_delay: float = 0.5):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts:
                        raise
                    time.sleep(base_delay * (2 ** (attempt - 1)))
        return wrapper
    return decorator
