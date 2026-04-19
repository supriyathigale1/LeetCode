# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/?envType=problem-list-v2&envId=hash-table
# Problem: Minimum Index Sum of Two Lists - Find restaurants with minimum index sum

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """
        Find all restaurants that appear in both lists with the minimum index sum.
        Index sum = index in list1 + index in list2
        
        Time Complexity: O(n + m) - create dictionaries and find intersections
        Space Complexity: O(n + m) - for the dictionaries
        
        Args:
            list1: First list of restaurants
            list2: Second list of restaurants
        
        Returns:
            List of restaurants with minimum index sum
        """}
        # Create index mappings for both lists
        index_map1 = {}
        index_map2 = {}
        
        for idx, restaurant in enumerate(list1):
            index_map1[restaurant] = idx
        
        for idx, restaurant in enumerate(list2):
            index_map2[restaurant] = idx
        
        # Find minimum index sum and collect all restaurants with that sum
        min_sum = float('inf')
        result = []
        
        # Check common restaurants (intersection)
        for restaurant in index_map1.keys() & index_map2.keys():
            current_sum = index_map1[restaurant] + index_map2[restaurant]
            
            if current_sum < min_sum:
                # Found new minimum, reset result
                min_sum = current_sum
                result = [restaurant]
            elif current_sum == min_sum:
                # Same minimum sum, add to result
                result.append(restaurant)
        
        return result