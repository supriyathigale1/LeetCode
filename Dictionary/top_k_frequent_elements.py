from collections import Counter

def top_k(nums, k):
    """
    Find the k most frequent elements in a list.

    Args:
        nums: List of integers
        k: Number of most frequent elements to return

    Returns:
        List of tuples (element, frequency) for the top k frequent elements
    """
    return Counter(nums).most_common(k)

# Example usage: Find top 2 most frequent elements
top_k([1, 1, 1, 2, 2, 3], 2)