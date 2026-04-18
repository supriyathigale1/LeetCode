from collections import Counter

def top_k(nums, k):
    return Counter(nums).most_common(k)

top_k([1,1,1,2,2,3], 2)