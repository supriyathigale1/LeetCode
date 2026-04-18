# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# Convert a Number to Hexadecimal
# Given a 32-bit signed integer, return its hexadecimal representation.

class Solution:
    def toHex(self, num: int) -> str:
        """
        Convert a 32-bit signed integer to its hexadecimal representation.

        Args:
            num: 32-bit signed integer

        Returns:
            Hexadecimal string representation

        Note:
            For negative numbers, two's complement representation is used.
            The result should not have leading zeros, except for the number 0.

        Time Complexity: O(1) since we process at most 32 bits
        Space Complexity: O(1)
        """
        # Handle edge case of zero
        if num == 0:
            return "0"

        # Mapping of decimal values to hexadecimal digits
        hex_map = {
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
        }

        result = ''

        # Convert to 32-bit unsigned representation using two's complement for negative numbers
        # This ensures we handle negative numbers correctly
        num &= 0xffffffff  # Mask to 32 bits

        # Convert to hexadecimal by repeatedly dividing by 16
        while num > 0:
            remainder = num % 16  # Get the least significant 4 bits
            result = hex_map[remainder] + result  # Prepend the hex digit
            num = num // 16  # Shift right by 4 bits (divide by 16)

        return result