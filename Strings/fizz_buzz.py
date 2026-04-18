# https://leetcode.com/problems/fizz-buzz
# Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:
# - answer[i] == "FizzBuzz" if i is divisible by 3 and 5
# - answer[i] == "Fizz" if i is divisible by 3
# - answer[i] == "Buzz" if i is divisible by 5
# - answer[i] == i (as a string) if none of the above conditions are true

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Generate FizzBuzz sequence up to n.

        Args:
            n: Upper limit for the sequence (inclusive)

        Returns:
            List of strings representing the FizzBuzz sequence from 1 to n

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Initialize answer array with size n+1 (index 0 unused)
        answer = [""] * (n + 1)

        # Fill the answer array from 1 to n
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                # Divisible by both 3 and 5
                answer[i] = 'FizzBuzz'
            elif i % 3 == 0:
                # Divisible by 3 only
                answer[i] = 'Fizz'
            elif i % 5 == 0:
                # Divisible by 5 only
                answer[i] = 'Buzz'
            else:
                # Not divisible by 3 or 5
                answer[i] = str(i)

        # Return the answer from index 1 to n (skip index 0)
        return answer[1:]