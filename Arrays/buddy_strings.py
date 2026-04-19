# https://leetcode.com/problems/buddy-strings/description/?envType=problem-list-v2&envId=hash-table
# Problem: Buddy Strings - Check if strings s and goal are buddy strings (can transform s to goal by swapping at most one pair)

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """
        Determine if s and goal are buddy strings.
        Two strings are buddy strings if we can swap exactly one pair of characters in s to get goal.
        Also, if s == goal and has duplicate characters, they are buddy strings.
        
        Time Complexity: O(n) - single pass through the strings
        Space Complexity: O(n) - for the diff list
        
        Args:
            s: First string
            goal: Target string
        
        Returns:
            True if s and goal are buddy strings, False otherwise
        """
        
        # Strings must be same length
        if len(s) != len(goal):
            return False
        
        # If strings are identical, check if s has duplicate characters
        if s == goal:
            # If there are duplicates, we can swap them to get goal (itself)
            if len(set(s)) < len(s):
                return True
            return False
        
        # Find all positions where s and goal differ
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        
        # Valid buddy strings must have exactly 2 differences that are swappable
        if len(diff) == 2:
            i, j = diff
            # Check if swapping positions i and j in s produces goal
            if s[i] == goal[j] and goal[i] == s[j]:
                return True
        
        return False