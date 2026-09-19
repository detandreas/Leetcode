class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        O(n) solution.

        Proof:
        let i = 0, j = len(height) - 1 and height[i] > height[j]
        then the curr_area = (j - i) * height[j] (we multiply by the min(height[i], height[j])).

        If we pin j = len(height) - 1, we can't get an (i, j) pair for which the area >= curr_area
        why?

        As we move i closer to j the (j - i) term gets smaller and the height term is always less that or equal to height[j],
        due to height = min(height[i], height[j])

        As a result the (j - i) term get's smaller while the height term at best stays the same, so the product get's smaller.
        That's why we can skip all those iterations and decrease j -= 1.

        The same holds if we pin i.
        """

        max_area = 0
        i, j = 0 , len(height) - 1

        while i < j:
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)

            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1

        return max_area
