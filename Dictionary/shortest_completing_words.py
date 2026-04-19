#https://leetcode.com/problems/shortest-completing-word/description/?envType=problem-list-v2&envId=hash-table
# Shortest Completing Word: Find shortest word containing all license plate letters
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Extract letters from license plate (case-insensitive)
        d={}
        c = Counter(ch for ch in licensePlate.lower() if ch.isalpha())
        print(f" LicensePlate is {c}")
        result=None
        # Find shortest word containing all required characters
        for s in words:
            f=Counter(s)
            valid=True
            print(f" word is {s}")
            for ch in c:
                if f[ch]<c[ch]:
                    valid=False
                    break
            if valid:
                if result is None or len(s)<len(result):
                    result=s
        return result