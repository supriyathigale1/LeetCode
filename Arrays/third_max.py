# https://leetcode.com/problems/third-maximum-number/?envType=problem-list-v2&envId=array
# Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Solution 1: Using sorting - Time O(n log n), Space O(n)
        # Remove duplicates and sort, then return third from end or max if less than 3 elements
        nums = list(set(nums))  # Remove duplicates
        nums.sort()  # Sort in ascending order

        if len(nums) < 3:
            return nums[-1]  # Return maximum (last element)
        return nums[-3]  # Return third maximum (third from end)

        # Solution 2: Single pass with three variables - Time O(n), Space O(1)
        # Track the top three maximum values using three variables
        first = second = third = float('-inf')

        for num in nums:
            # Skip if we've already seen this number as one of the top three
            if num == first or num == third or num == second:
                print(f"continue {num}")
                continue

            if num > first:
                # New first maximum, shift others down
                first, second, third = num, first, second
                print(f"first {first}, second={second}, third={third}")
            elif num > second:
                # New second maximum, shift third down
                second, third = num, second
                print(f"second={second}, third={third}")
            elif num > third:
                # New third maximum
                third = num
                print(f"third={third}")

        # Return third if it exists, otherwise return first (maximum)
        if third != float('-inf'):
            return third
        else:
            return first