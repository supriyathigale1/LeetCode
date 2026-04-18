class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Find all numbers that disappeared in the array.
        Given an array nums of n integers where nums[i] is in the range [1, n],
        return an array of all the integers in the range [1, n] that do not appear in nums.

        This solution uses O(1) extra space by modifying the input array in-place.
        """

        # Alternative solution using extra space (commented out)
        """
        s = set(nums)  # Convert to set for O(1) lookups
        n = len(nums)
        lst = []
        print(f"nums is {s}")
        for i in range(1, n+1):  # Check numbers from 1 to n
            if i not in s:
                lst.append(i)
        print(lst)
        return lst
        """

        # In-place solution: Mark presence by negating values at corresponding indices
        # For each number, use its absolute value - 1 as index and negate that position
        for num in nums:
            idx = abs(num) - 1  # Get the index (0-based) for this number
            nums[idx] = -abs(nums[idx])  # Mark as visited by making negative

        print(nums)  # Debug: show the modified array

        # Collect missing numbers: positions that are still positive
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:  # If positive, that index+1 was never marked (missing number)
                result.append(i + 1)  # Convert back to 1-based numbering

        return result