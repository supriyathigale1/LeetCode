# https://leetcode.com/problems/next-greater-element-i/description/?envType=problem-list-v2&envId=array
# Problem: Next Greater Element I - Find the next greater element for each element in nums1

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the next greater element for each element in nums1 as it appears in nums2.
        Uses a monotonic stack to efficiently track greater elements.
        
        Time Complexity: O(n + m) - each element is pushed/popped once
        Space Complexity: O(m) - for the stack and hash map
        
        Args:
            nums1: List of elements to find next greater elements for
            nums2: List containing all elements of nums1 (reference list)
        
        Returns:
            List of next greater elements (-1 if no greater element exists)
        """
        # Use monotonic stack to track next greater elements
        stack = []  # Stack to maintain decreasing order
        element_map = {}  # Map element to its next greater element
        result = []
        
        # Process each element in nums2
        for num in nums2:
            # Pop all elements smaller than current number
            # They have found their next greater element
            while stack and stack[-1] < num:
                candidate = stack.pop()
                element_map[candidate] = num
            
            # Add current element to stack
            stack.append(num)
        
        # Remaining elements in stack have no greater element
        while stack:
            element_map[stack.pop()] = -1
        
        # Build result for nums1
        for num in nums1:
            result.append(element_map[num])
        
        return result