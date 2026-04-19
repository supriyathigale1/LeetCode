#https://leetcode.com/problems/degree-of-an-array/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Count frequency of each element
        freq = Counter(nums)
        
        # Track first and last occurrence of each element
        first_occurrence = {}
        last_occurrence = {}
        
        # Initialize answer to length of array
        min_length = len(nums)
        
        # Find the degree (maximum frequency)
        degree = max(freq.values())
        
        # Record first and last positions of each element
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i
        
        # Find shortest subarray containing elements with max frequency
        for num in freq:
            if freq[num] == degree:
                # Length from first to last occurrence (inclusive)
                length = last_occurrence[num] - first_occurrence[num] + 1
                min_length = min(min_length, length)
        
        return min_length
        