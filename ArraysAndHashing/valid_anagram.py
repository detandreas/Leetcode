class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        O(nlgn + mlgm):
        return sorted(s) == sorted(t)

        Current solution is O(n + m)
        """
        
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            freq[index] += 1
        for c in t:
            index = ord(c) - ord('a')
            freq[index] -= 1

        return all(f == 0 for f in freq)
    