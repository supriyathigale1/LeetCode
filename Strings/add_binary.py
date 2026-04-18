# https://leetcode.com/problems/add-binary
# Add Binary
# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Add two binary strings and return their sum as a binary string.

        Args:
            a: First binary string
            b: Second binary string

        Returns:
            Sum of a and b as a binary string

        Time Complexity: O(max(len(a), len(b)))
        Space Complexity: O(max(len(a), len(b)))
        """
        # Pad the shorter string with leading zeros to make them equal length
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0  # Carry from addition
        result = ""  # Build result string

        # Iterate from right to left (least significant bit to most)
        for i in range(len(a) - 1, -1, -1):
            # Sum of current bits plus carry
            total = int(a[i]) + int(b[i]) + carry
            carry = total // 2  # New carry (0 or 1)
            bit = total % 2  # Current bit (0 or 1)
            result = str(bit) + result  # Prepend to result

        # If there's a remaining carry, add it as the most significant bit
        if carry:
            result = '1' + result

        return result