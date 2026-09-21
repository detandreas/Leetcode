import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        O(n) time complexity
        O(1) space complexity
        """

        if sum(nums) < target:
            return 0

        min_len = sys.maxsize
        i = j = 0
        window_sum = nums[i]
        while j < len(nums):

            if window_sum >= target:
                min_len = min(j - i + 1, min_len)
                window_sum -= nums[i]
                i += 1
                continue

            j += 1
            if j < len(nums):
                window_sum += nums[j]

        return min_len

s = Solution()
nums = [5, 1]
print(s.minSubArrayLen(5, nums))
