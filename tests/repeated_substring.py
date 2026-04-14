#https://leetcode.com/problems/repeated-substring-pattern/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        #For a substring to be repeated, its length must be a factor of the length of the original string. So we only need to check for factors of n.
        for i in range(1,n//2+1):
            
            if n%i==0:
                pattern=s[:i]
                print(i,pattern)
                if pattern*(n//i)==s:
                    return True
        return False