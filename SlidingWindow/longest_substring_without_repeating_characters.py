class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        O(n) time complexity
        O(n) space complexity
        """

        if not s: return 0

        hash_map = {}
        i, j = 0, 1
        hash_map[s[i]] = 1
        max_len = 0

        while j < len(s):

            if s[j] in hash_map:
                max_len = max(max_len, j - i)
                del hash_map[s[i]]
                i += 1
                if i == j:
                    j += 1
                    hash_map[s[i]] = 1
                continue

            hash_map[s[j]] = 1
            j += 1

        return max(max_len, j - i)