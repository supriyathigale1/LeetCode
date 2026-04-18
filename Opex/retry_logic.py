import time

def retry(func, retries=3, delay=2):
    """
    Retry a function call with exponential backoff on failure.

    Args:
        func: The function to retry (should be a callable with no arguments)
        retries: Number of retry attempts (default: 3)
        delay: Delay in seconds between retries (default: 2)

    Returns:
        The result of the successful function call

    Raises:
        Exception: If all retry attempts fail
    """
    for attempt in range(retries):
        try:
            return func()  # Attempt to call the function
        except Exception:
            time.sleep(delay)  # Wait before retrying
    raise Exception("Failed after retries")  # All attempts failed