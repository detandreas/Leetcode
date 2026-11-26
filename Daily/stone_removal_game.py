class Solution:
    def canAliceWin(self, n: int) -> bool:

        remove = 10
        count = 0
        while n >= remove:
            count += 1
            n -= remove
            remove -= 1
        return count % 2 == 1

