#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # This solution is O(n) time complexity, which is not optimal for sorted arrays.
        s=[]
        for x in range(len(nums)):
            if nums[x]==target:
                s.append(x)
        print(s)
        if s:
            return [s[0],s[-1]]
        else:
            return [-1,-1]
        
        #