# https://leetcode.com/problems/excel-sheet-column-title/
# Excel Sheet Column Title
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        Convert a column number to its Excel column title (A, B, C, ..., Z, AA, AB, etc.)

        Args:
            columnNumber: The column number (1-based)

        Returns:
            Excel column title as string

        Example:
            1 -> "A", 26 -> "Z", 27 -> "AA", 52 -> "AZ"

        Time Complexity: O(log n) where n is columnNumber
        Space Complexity: O(log n)
        """
        # Mapping of remainders to letters (0-based indexing)
        letter_map = {
            0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
            10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
            19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
        }

        result = ""

        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-based to 0-based indexing
            remainder = columnNumber % 26  # Get the current letter index
            result = letter_map[remainder] + result  # Prepend the letter
            columnNumber = columnNumber // 26  # Move to next digit

        return result
