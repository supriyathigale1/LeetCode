#https://leetcode.com/problems/next-greater-element-i/description/?envType=problem-list-v2&envId=array
# Next Greater Element I: Find next greater element for each element in nums1
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use monotonic stack to efficiently track next greater elements
        lst=[]
        map={}
        result=[]
        # Process each element in nums2
        for num in nums2:
            # Pop all elements smaller than current number from stack
            while lst and lst[-1]<num:
                candidate=lst.pop()
                map[candidate]=num
            lst.append(num)

        # Remaining elements in stack have no greater element
        while lst:
            map[lst.pop()]=-1
        
        # Build result for nums1
        for num in nums1:
            result.append(map[num])
        return result