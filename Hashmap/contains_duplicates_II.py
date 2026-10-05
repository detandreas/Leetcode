class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        O(n) time complexity
        O(n) space complexity
        """
        hash_map = {}
        for j, num in enumerate(nums):

            if num in hash_map and j - hash_map[num] <= k:
                    return True

            hash_map[num] = j
        return False