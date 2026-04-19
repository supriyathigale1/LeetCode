#https://leetcode.com/problems/distribute-candies/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Get unique candy types
        unique_candies = set(candyType)
        
        # Maximum candies Alice can eat
        max_candies = len(candyType) // 2
        
        # She can eat at most min(unique types, max_candies)
        # If unique types <= max_candies, she gets all unique types
        # If unique types > max_candies, she gets max_candies different types
        return min(len(unique_candies), max_candies)
        