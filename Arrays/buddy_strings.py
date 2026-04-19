#https://leetcode.com/problems/buddy-strings/description/?envType=problem-list-v2&envId=hash-table
# Buddy Strings: Check if two strings are "buddy strings" (swap one pair to match)
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Strings must have equal length to be buddy strings
        if len(s)!=len(goal):
            return False
        # If strings are equal, check if there are duplicate characters to swap
        if s==goal:
            if len(set(s))<len(s):
                return True
        # Find all positions where s and goal differ
        diff=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                diff.append(i)
        print(f"diff is {diff}")
        # Valid buddy strings have exactly 2 differences that can be swapped
        if len(diff)==2:
            i,j=diff
            if s[i]==goal[j] and goal[i]==s[j]:
                return True
        return False