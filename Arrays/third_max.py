#https://leetcode.com/problems/third-maximum-number/?envType=problem-list-v2&envId=array
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #Time complexity O(n log n) due to sorting, space complexity O(n) due to creating a new list for unique elements.
        nums = list(set(nums))   # remove duplicates
        nums.sort()   
         
        if len(nums) < 3:
            return nums[-1]      # max
        return nums[-3] 
    
        
        first=second=third=float('-inf')
        for num in nums:
            if num==first or num==third or num==second:
                print(f"continue {num}")
                continue
            if num>first:
                first,second,third=num,first,second
                print(f"first {first}, second={second}, third ={third}")
            elif num>second:
                second,third=num,second
                print(f" second={second}, third ={third}")
            elif num>third:
                third=num
                print(f"third ={third}")
        if third!=float('-inf'):
            return third
        else:
            return first