from collections import defaultdict, Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        m = |ransomNote|
        n = |magazine|

        O(m + n) time complexity
        O(26) = O(1) space complexity
        """
        hashmap: dict[str, int] = defaultdict(int)

        for c in magazine:
            hashmap[c] += 1

        for c in ransomNote:

            if hashmap[c] <= 0:
                return False

            hashmap[c] -= 1

        return True

class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))

s = Solution2()
ransomNote = "aa"
magazine = "aab"
s.canConstruct(ransomNote, magazine)