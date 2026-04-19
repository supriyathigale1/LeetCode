#https://leetcode.com/problems/jewels-and-stones/description/?envType=problem-list-v2&envId=hash-table
# Jewels and Stones: Count how many stones are jewels (case-sensitive)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Create counters for jewels and stones
        c=Counter(jewels)
        c2=Counter(stones)
        total=0
        # Count stones that are jewels
        for x in c:
            if x in c2:
                total=total+c2[x]
        return total