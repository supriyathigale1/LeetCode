import time

def retry(func, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return func()
        except Exception:
            time.sleep(delay)
    raise Exception("Failed after retries")