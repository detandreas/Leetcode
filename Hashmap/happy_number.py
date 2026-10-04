class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        seen.add(n)

        while True:
            sum = 0

            while n > 0:
                d = n % 10
                sum += d**2
                n = n // 10

            if sum == 1:
                return True

            if sum in seen:
                return False

            seen.add(sum)
            n = sum

class Solution2:
    def isHappy(self, n: int) -> bool:
        """Same solution better code."""
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            while n > 0:
                n, d = divmod(n, 10)
                total += d * d
            n = total

        return n == 1


s = Solution()
n = 19
s.isHappy(n)