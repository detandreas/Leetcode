class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        O(nlgn) time complexity
        O(n) space complexity
        """

        intervals.sort(key=lambda l: l[0])
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # Otherwise there is a overlap.
            # Perform the merge by updating the upper value.
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


s = Solution()
intervals = [[1, 3], [8, 10], [15, 18], [2, 6]]
print(s.merge(intervals))
