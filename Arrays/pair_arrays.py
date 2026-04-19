#https://leetcode.com/problems/array-partition/?envType=problem-list-v2&envId=array
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n=len(nums)/2 #number of pairs
        m=0
        nums.sort()
        total=0
        print(f"sorted array is {nums}")
        for i in range(0,len(nums),2):
            total+=nums[i]
        print(f"total is {total}")
        return total
    
    #Alternate solution
        n = len(nums) // 2   # FIX 1: integer division
        m = 0
        
        nums.sort()
        total = 0            # FIX 2: avoid using built-in name sum
        
        print(f"sorted array is {nums}")
        
        for i in range(0, len(nums), 2):   # FIX 3: step by 2 to form pairs
            if m < n:
                total += min(nums[i], nums[i+1])  # FIX 4: proper pair min
                m += 1
        
        print(f"sum is {total}")
        return total
    
#Runtime: 88 ms, faster than 99.97% of Python3 online submissions for Array Partition.
