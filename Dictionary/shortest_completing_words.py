#https://leetcode.com/problems/shortest-completing-word/description/?envType=problem-list-v2&envId=hash-table
# Problem: Shortest Completing Word - Find the shortest word that contains all letters from license plate

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        """
        Find the shortest word that contains all letters (case-insensitive) from license plate.
        Ignores numbers and special characters.
        
        Time Complexity: O(n*m) - where n is number of words, m is average word length
        Space Complexity: O(1) - character frequencies bounded by alphabet size
        
        Args:
            licensePlate: License plate string containing letters and numbers
            words: List of candidate completing words
        
        Returns:
            The shortest word that contains all required letters
        """
        # Extract letters from license plate (case-insensitive, ignore non-alphabetic)
        required_chars = Counter(ch for ch in licensePlate.lower() if ch.isalpha())
        
        result = None
        
        # Check each word
        for word in words:
            # Count characters in current word
            word_chars = Counter(word)
            
            # Check if word contains all required characters
            valid = True
            for char in required_chars:
                if word_chars[char] < required_chars[char]:
                    valid = False
                    break
            
            # Update result if this is a valid word and shorter than current result
            if valid:
                if result is None or len(word) < len(result):
                    result = word
        
        return result