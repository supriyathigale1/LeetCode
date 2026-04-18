# https://leetcode.com/problems/range-sum-query-immutable
# Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries of the form:
# sumRange(i, j) which returns the sum of the elements from index i to j inclusive.

class NumArray:
    """
    A class to efficiently handle range sum queries on an immutable array.
    Note: This implementation uses O(n) time per query, which is not optimal.
    A more efficient approach would use prefix sums for O(1) query time.
    """

    def __init__(self, nums: List[int]):
        """
        Initialize the NumArray with the given array.

        Args:
            nums: The input array of integers
        """
        self.nums = nums  # Store the original array

        # Note: The following code in the original seems incorrect and is commented out
        # It appears to be trying to precompute something but has logical errors
        """
        lst = []
        for x in range(len(nums)):
            if nums[x] == 'sumRange':  # This condition doesn't make sense for integer arrays
                s = sumRange(self, nums[x][0], nums[x][1])  # nums[x] is an int, not a list
                lst.append(s)
            else:
                lst.append(None)
        print(lst)
        """

    def sumRange(self, left: int, right: int) -> int:
        """
        Calculate the sum of elements from index left to right inclusive.

        Args:
            left: Starting index (inclusive)
            right: Ending index (inclusive)

        Returns:
            Sum of elements in the range [left, right]

        Time Complexity: O(n) where n = right - left + 1
        """
        summ = 0
        for i in range(left, right + 1):
            summ = self.nums[i] + summ
        return summ

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left, right)