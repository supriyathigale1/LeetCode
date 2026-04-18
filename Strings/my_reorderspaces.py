# Alternative implementation for rearranging spaces between words
# https://leetcode.com/problems/rearrange-spaces-between-words

class Solution:
    def reorderSpaces(self, text: str) -> str:
        """
        Rearrange spaces between words evenly, with extra spaces at the end.

        Args:
            text: Input string with words and spaces

        Returns:
            String with spaces rearranged evenly between words

        Time Complexity: O(n) where n is length of text
        Space Complexity: O(n)
        """
        # Count total spaces in the text
        total_spaces = text.count(' ')

        # Split text into words (removes extra spaces)
        words = text.split()
        num_words = len(words)

        if num_words == 1:
            # If only one word, put all spaces at the end
            return words[0] + ' ' * total_spaces

        # Calculate spaces between words and extra spaces at end
        spaces_between = total_spaces // (num_words - 1)
        extra_spaces = total_spaces % (num_words - 1)

        # Build result string
        result = ""
        for i in range(num_words):
            result += words[i]  # Add current word

            # Add spaces between words (except after last word)
            if i != num_words - 1:
                result += ' ' * spaces_between

        # Add remaining spaces at the end
        result += ' ' * extra_spaces

        return result
            
        



