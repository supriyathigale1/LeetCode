def chunk_data(data, chunk_size):
    """
    Generator function to split data into fixed-size chunks.

    Args:
        data: The data to be chunked (list, string, etc.)
        chunk_size: Size of each chunk

    Yields:
        Chunks of the original data, each of size chunk_size (except possibly the last)

    Example:
        list(chunk_data([1,2,3,4,5], 2)) -> [[1,2], [3,4], [5]]
    """
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]