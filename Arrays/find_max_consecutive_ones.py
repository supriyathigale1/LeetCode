#https://leetcode.com/problems/max-consecutive-ones/?envType=problem-list-v2&envId=array
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        can=0
        #time complexity O(n)
        for x in nums:
            if x==1:
                l=l+1
            else:
                can=max(can,l)
                l=0
        can=max(can,l)
        
        return can