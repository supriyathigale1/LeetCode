# https://leetcode.com/problems/excel-sheet-column-number/
# Excel Sheet Column Number
# Given a string columnTitle that represents the column title as appears in an Excel sheet,
# return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Convert Excel column title to its corresponding column number.

        Args:
            columnTitle: Excel column title (e.g., "A", "B", "Z", "AA", "AB")

        Returns:
            Column number as integer (1-based)

        Example:
            "A" -> 1, "Z" -> 26, "AA" -> 27, "AZ" -> 52

        Time Complexity: O(n) where n is length of columnTitle
        Space Complexity: O(1)
        """
        # Mapping of letters to their numeric values (A=1, B=2, ..., Z=26)
        letter_to_num = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
            'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
            'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
            'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
            'Z': 26
        }

        result = 0

        # Process each character from left to right
        # This is like converting from base-26 to decimal
        for char in columnTitle:
            result = result * 26 + letter_to_num[char]

        return result