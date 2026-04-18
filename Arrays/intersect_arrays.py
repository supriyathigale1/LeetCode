#https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=Counter(nums1)
        result=[]
        for n in nums2:
            print(c[n],c)
            if c[n]>0:
                result.append(n)
                c[n]-=1
        print(result)
        return result

