#https://leetcode.com/problems/degree-of-an-array/description/?envType=problem-list-v2&envId=hash-table
# Degree of Array: Find shortest subarray with same degree as input
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Count frequency of each element
        freq=Counter(nums)
        # Track first and last occurrence
        first={}
        last={}
        ans=len(nums)
        # Find the degree (maximum frequency)
        degree=max(freq.values())
        # Record first and last positions
        for i,num in enumerate(nums):
            if num not in first:
                first[num]=i
            last[num]=i
        
        # Find shortest subarray with elements having max frequency
        for num in freq:
            if freq[num]==degree:
                length=last[num]-first[num]+1
                ans=min(ans,length)
        return ans
        
        