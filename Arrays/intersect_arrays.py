# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result should appear as many times as it shows in both arrays.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use Counter to count frequency of each number in nums1
        c = Counter(nums1)

        # Initialize result list
        result = []

        # Iterate through nums2 and check if each number exists in nums1's counter
        for n in nums2:
            print(c[n], c)  # Debug: print current count and full counter
            if c[n] > 0:  # If count > 0, this number appears in both arrays
                result.append(n)  # Add to result
                c[n] -= 1  # Decrement count to handle duplicates correctly

        print(result)  # Debug: print final result
        return result

