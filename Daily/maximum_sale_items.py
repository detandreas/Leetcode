class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        """
        Pattern to remember: when an item's first unit is worth more than later units,
        split it into a 0/1 "first copy" choice plus an unbounded "more copies" choice,
        and give the second one a same-row transition.
        """
        n = len(items)

        # free[i] = free copies gained by buying >= 1 copy of item i (0-indexed)
        free = [0] * n
        for i in range(n):
            f = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % f == 0:
                    free[i] += 1

        # dp[i][b] = max copies using the first i items with budget b
        dp = [[0] * (budget + 1) for _ in range(n + 1)]   # row 0 = base case

        for i in range(1, n + 1):
            price = items[i - 1][1]
            bonus = free[i - 1]
            for b in range(budget + 1):
                best = dp[i - 1][b]                          # skip item i
                for x in range(1, b // price + 1):           # buy x >= 1 copies
                    best = max(best, dp[i - 1][b - x * price] + x + bonus)
                dp[i][b] = best

        return dp[n][budget]

s = Solution()
items = [[6, 2], [2, 6], [3, 4]]
budget = 9
print(s.maximumSaleItems(items, budget))
