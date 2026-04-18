# https://leetcode.com/problems/max-consecutive-ones/?envType=problem-list-v2&envId=array
# Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Find the maximum number of consecutive 1's in a binary array.

        Args:
            nums: List of binary integers (0s and 1s)

        Returns:
            Maximum count of consecutive 1's

        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - constant extra space
        """
        l = 0  # Current streak of consecutive 1's
        can = 0  # Maximum streak found so far

        for x in nums:
            if x == 1:
                l = l + 1  # Increment current streak
            else:
                can = max(can, l)  # Update maximum if current streak is larger
                l = 0  # Reset current streak

        # Final check in case the longest streak is at the end
        can = max(can, l)

        return can