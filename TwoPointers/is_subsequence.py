class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """t: i, s: j"""

        if len(s) > len(t):
            return False

        target = len(s)
        i, j = 0, 0

        while i < len(t) and j < target:

            if t[i] == s[j]:
                j += 1

            i += 1

        return j == target

sol = Solution()
s = "acb"
t = "ahbgdc"
print(sol.isSubsequence(s, t))