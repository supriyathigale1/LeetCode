# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Solution 1: Linear search - O(n) time complexity
        # This approach works but is not optimal for sorted arrays
        s = []  # Store indices where target is found
        for x in range(len(nums)):
            if nums[x] == target:
                s.append(x)
        print(s)  # Debug: print all indices
        if s:
            return [s[0], s[-1]]  # Return first and last occurrence
        else:
            return [-1, -1]  # Target not found

        # Solution 2: Binary search - O(log n) time complexity (Optimal for sorted arrays)
        # Use two binary searches: one to find leftmost occurrence, one for rightmost
        def find_left():
            l, r = 0, len(nums) - 1
            left = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    left = mid
                    r = mid - 1  # Continue searching left for first occurrence
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return left

        def find_right():
            l, r = 0, len(nums) - 1
            right = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    right = mid
                    l = mid + 1  # Continue searching right for last occurrence
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return right
        
        return [find_left(), find_right()]