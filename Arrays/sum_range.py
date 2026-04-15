#https://leetcode.com/problems/range-sum-query-immutable
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        lst=[]
        
        for x in range(len(nums)):
            if nums[x]=='sumRange':
                s=sumRange(self,nums[x][0],nums[x][1])
                lst.append(s)
            else:
                lst.append(None)
        print(lst)

    def sumRange(self, left: int, right: int) -> int:
        summ=0
        for i in range(left,right+1):
            summ=self.nums[i]+summ
        return summ

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)