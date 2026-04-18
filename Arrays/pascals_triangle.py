# https://leetcode.com/problems/pascals-triangle/
# Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generate the first numRows of Pascal's triangle.

        Args:
            numRows: Number of rows to generate

        Returns:
            List of lists representing Pascal's triangle rows

        Example:
            generate(5) returns:
            [
                [1],
                [1,1],
                [1,2,1],
                [1,3,3,1],
                [1,4,6,4,1]
            ]
        """
        lst = []  # Store the triangle rows
        k = 0

        for x in range(numRows):
            if x == 0:
                # First row is always [1]
                lst.append([1])
            elif x == 1:
                # Second row is always [1,1]
                lst.append([1, 1])
            else:
                # For subsequent rows, each element is sum of two elements above
                k = 0
                l = [1]  # Start with 1
                # Calculate middle elements by summing adjacent elements from previous row
                while k < len(lst[x-1]) - 1:
                    l.append(lst[x-1][k] + lst[x-1][k+1])
                    k = k + 1
                l.append(1)  # End with 1
                lst.append(l)

        print(lst)  # Debug output
        return lst

