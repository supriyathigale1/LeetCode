class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Code with extra space 
        """ s=set(nums)
        n=len(nums)
        lst=[]
        print(f"nums is {s}")
        for i in range(1,n+1):
            if i not in s:
                lst.append(i)
        print(lst)
        return lst """

        #Touching each number
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
            
        print(nums)

        # collect missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
                
        return result