#https://leetcode.com/problems/longest-harmonious-subsequence/?envType=problem-list-v2&envId=array
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Count frequency of each number
        count = Counter(nums)
        
        max_length = 0
        
        # For each unique number, check if number+1 exists
        for num in count:
            if num + 1 in count:
                # Length of harmonious pair = count(num) + count(num+1)
                current_length = count[num] + count[num + 1]
                max_length = max(max_length, current_length)
        
        return max_length