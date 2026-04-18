# https://leetcode.com/problems/repeated-substring-pattern/
# Repeated Substring Pattern
# Given a string s, check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Check if string can be formed by repeating a substring.

        Args:
            s: Input string to check

        Returns:
            True if string consists of repeated substring, False otherwise

        Time Complexity: O(n^2) in worst case, but typically better
        Space Complexity: O(1) excluding input
        """
        n = len(s)

        # For a substring to repeat and form the whole string,
        # its length must be a divisor of the total length
        # We only need to check divisors of n

        # Check all possible substring lengths that are divisors of n
        for i in range(1, n // 2 + 1):
            if n % i == 0:  # i is a divisor of n
                pattern = s[:i]  # Take substring of length i
                print(i, pattern)  # Debug output

                # Check if repeating this pattern gives the original string
                if pattern * (n // i) == s:
                    return True

        return False