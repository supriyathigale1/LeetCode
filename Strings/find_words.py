# https://leetcode.com/problems/keyboard-row/
# Keyboard Row
# Given an array of strings words, return the words that can be typed using
# letters of the alphabet on only one row of American keyboard.

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        Find words that can be typed using only one row of the keyboard.

        Args:
            words: List of words to check

        Returns:
            List of words that can be typed on a single keyboard row

        Time Complexity: O(n*m) where n is number of words, m is average word length
        Space Complexity: O(n) for result list
        """
        # Define the three keyboard rows
        row1 = 'qwertyuiop'  # Top row
        row2 = 'asdfghjkl'   # Middle row
        row3 = 'zxcvbnm'     # Bottom row

        result = []

        for word in words:
            w = word.lower()  # Convert to lowercase for case-insensitive comparison

            # Flags to track if word can be typed on each row
            can_use_row1 = True
            can_use_row2 = True
            can_use_row3 = True

            # Check if all letters are in row 1
            for char in w:
                if char not in row1:
                    can_use_row1 = False
                    break

            # Check if all letters are in row 2
            for char in w:
                if char not in row2:
                    can_use_row2 = False
                    break

            # Check if all letters are in row 3
            for char in w:
                if char not in row3:
                    can_use_row3 = False
                    break

            # If word can be typed on any single row, add it to result
            if can_use_row1 or can_use_row2 or can_use_row3:
                result.append(word)

        return result