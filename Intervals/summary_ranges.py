class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        def fmt(a: int, b: int) -> str:
            return str(a) if a == b else f"{a}->{b}"

        res = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i - 1]:
                res.append(fmt(start, nums[i - 1]))
                start = nums[i]

        res.append(fmt(start, nums[-1]))
        return res


s = Solution()
nums = [0, 1, 2, 4, 5, 7]
s.summaryRanges(nums)


class Solution2:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        """
        Better approach
        O(n) time complexity
        O(1) space complexity
        """
        res = []
        i, n = 0, len(nums)
        while i < n:
            j = i
            while j + 1 < n and nums[j] + 1 == nums[j + 1]:
                j += 1
            res.append(str(nums[i]) if i == j else f"{nums[i]}->{nums[j]}")
            i = j + 1
        return res
