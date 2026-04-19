# https://leetcode.com/problems/jewels-and-stones/description/?envType=problem-list-v2&envId=hash-table
# Problem: Jewels and Stones - Count how many stones are jewels (case-sensitive)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Count the number of stones that are also jewels (case-sensitive).
        
        Time Complexity: O(n + m) - where n is length of jewels, m is length of stones
        Space Complexity: O(n) - for the counter of jewels
        
        Args:
            jewels: String representing jewel characters
            stones: String representing stone characters collected
        
        Returns:
            Count of how many stones are jewels
        """
        # Create counters for both jewels and stones
        jewel_counts = Counter(jewels)
        stone_counts = Counter(stones)
        
        # Count stones that are jewels
        total = 0
        for jewel in jewel_counts:
            if jewel in stone_counts:
                # Add count of this jewel type found in stones
                total += stone_counts[jewel]
        
        return total