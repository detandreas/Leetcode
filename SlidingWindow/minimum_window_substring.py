from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Implementation based on the observation that we only need to traverse the characters is that appear in t.
        Those characters and their indexes are stored in filterd.

        i.e
        s = "ADOBECODEBANC", t = "ABC"
        filtered = [(0, 'A'), (3, 'B'), (5, 'C'), (9, 'B'), (10, 'A'), (12, 'C')]

        Requires preprocessing of s!!!
        Same overall complexity, in fact the second solution scores higher in leetcode.
        """
        need = Counter(t)
        required = len(need)
        filtered = [(i, ch) for i, ch in enumerate(s) if ch in need]

        window: dict[str, int] = defaultdict(int)
        formed = 0
        l = 0
        best = (float("inf"), 0, 0)  # (length, start, end)

        for r in range(len(filtered)):
            idx_r, ch = filtered[r]
            window[ch] +=  1
            if window[ch] == need[ch]:
                formed += 1

            while formed == required:
                idx_l, left_ch = filtered[l]
                if idx_r - idx_l + 1 < best[0]:
                    best = (idx_r - idx_l + 1, idx_l, idx_r)
                window[left_ch] -= 1
                if window[left_ch] < need[left_ch]:
                    formed -= 1
                l += 1

        return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]

from collections import Counter, defaultdict

class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        required = len(need)
        window: dict[str, int] = defaultdict(int)
        formed = 0

        best_len = float("inf")
        best_l = 0
        l = 0

        for r, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l

                left_ch = s[l]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]