#https://leetcode.com/problems/longest-harmonious-subsequence/?envType=problem-list-v2&envId=array
# Longest Harmonious Subsequence: Find longest subsequence with max difference of 1
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Count frequency of each number
        c=Counter(nums)
        freq=0
        best=0
        # For each unique number, check if number+1 exists
        for x,y in c.items():
            if x+1 in c:
                freq=y+c[x+1]
                best=max(freq,best)
                

        return best