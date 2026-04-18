# https://leetcode.com/problems/crawler-log-folder/
# Crawler Log Folder
# The LeetCode file system keeps a log each time some user performs a change folder operation.
# The operations are described below:
# - "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
# - "./" : Remain in the same folder.
# - "x/" : Move to the child folder named x (This folder is guaranteed to always exist).

from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        Calculate the minimum number of operations to return to the main folder.

        Args:
            logs: List of folder operations

        Returns:
            Minimum operations needed to reach main folder (depth from root)

        Time Complexity: O(n) where n is length of logs
        Space Complexity: O(1)
        """
        depth = 0  # Current folder depth from root

        for operation in logs:
            if operation == './':
                # Stay in current folder - no change
                pass
            elif operation == '../':
                # Move to parent folder (decrease depth, but not below 0)
                depth = max(0, depth - 1)
            else:
                # Move to child folder (increase depth)
                depth = depth + 1

        # Return final depth (minimum operations to reach root would be this depth)
        return depth