#https://leetcode.com/problems/distribute-candies/description/?envType=problem-list-v2&envId=hash-table
# Distribute Candies: Maximize distinct candy types Alice can eat
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Get unique candy types
        c=set(candyType) # set of candies by each type
        n=len(candyType)//2 #number of candies she can eat
        print(f"Candy types {c} and number of candies {n}")
        result=0
        
        # Count unique candy types
        for x in c:
            result=result+1
        # Return minimum of unique types and max candies allowed
        if n==result:
            return result
        elif n>result:
            return result
        else:
            return n
        