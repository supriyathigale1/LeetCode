# https://leetcode.com/problems/add-strings
# Add Strings
# Given two non-negative integers, num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Add two numbers represented as strings without converting to integers.

        Args:
            num1: First number as string
            num2: Second number as string

        Returns:
            Sum of num1 and num2 as a string

        Time Complexity: O(max(len(num1), len(num2)))
        Space Complexity: O(max(len(num1), len(num2)))
        """
        # Pad the shorter string with leading zeros
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        carry = 0  # Carry from addition
        result = ""  # Build result string

        # Iterate from right to left
        for i in range(len(num1) - 1, -1, -1):
            # Sum of current digits plus carry
            total = int(num1[i]) + int(num2[i]) + carry
            carry = total // 10  # New carry (0-1)
            digit = total % 10  # Current digit (0-9)
            result = str(digit) + result  # Prepend to result

        # If there's a remaining carry, add it
        if carry:
            result = str(carry) + result

        # Handle edge case of both numbers being zero
        if num1 == '0' and num2 == '0':
            return '0'

        return result
