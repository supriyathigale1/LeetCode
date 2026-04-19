#https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=Counter(allowed)
        cnt=0
        for word in words:
            f=Counter(word)
            valid=True
            for ch in word:
                if ch not in c:
                    valid=False
                    break
            if valid:
                cnt=cnt+1
        return cnt
                