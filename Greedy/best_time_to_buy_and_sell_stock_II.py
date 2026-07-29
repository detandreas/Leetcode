class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        profits = [0] * len(prices)
        buy = prices[0]
        sell = 0
        sell_day = -1
        total_profit = 0
        for i in range(1, len(prices)):

            if prices[i] < buy:
                buy = prices[i]
                sell = 0
                if sell_day >= 0:
                    total_profit += profits[sell_day]
                sell_day = -1
                continue

            if prices[i] > sell:
                sell = prices[i]
                profit = sell - buy
                profits[i] = profit
                sell_day = i

            if prices[i] < sell:
                buy = prices[i]
                sell = 0
                if sell_day >= 0:
                    total_profit += profits[sell_day]
                sell_day = -1
        
        if sell_day >= 0:
                    total_profit += profits[sell_day]

        return total_profit

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Greedy algorithm.

        Sum every positive day-to-day delta, equivalent to buying at local minimum and
        selling at the local maximum.

        e.g. [1,3,6] you want to buy at 1 and sell at 6, achieving a profit of 6-1=5.
        (3-1) + (6-3) = 2 + 3 = 5, same using day-to-day delta.

        """
        
        profit = 0
        for i in range(1, len(prices)):
             if prices[i] > prices[i-1]:
                  profit += prices[i] - prices[i-1]

        return profit

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Dynamic Programming.
        """

        n = len(prices)

        f = [[0, 0] for _ in range(n)]

        # f[i][0] = no χωρίς μετοχή στο τέλος της μέρας i
        # f[i][1] = με μετοχή στο τέλος της μέρας i
        f[0][0] = 0
        f[0][1] = -prices[0]

        for i in range(1, n):
            f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i])
            f[i][1] = max(f[i-1][1], f[i-1][0] - prices[i])
        
        return f[n-1][0]


s = Solution()
#prices = [7,1,5,3,6,4]
#prices = [1,2,3,4,5]
#prices = [7,6,4,3,1]
#prices = [7,1,3,5,4,6]
prices = [11, 5, 11, 11, 6, 8, 2, 5]
print(s.maxProfit(prices))