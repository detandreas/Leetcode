class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = [0] * 26

        for c in s + t:
            index = ord(c) - ord('a')
            freq[index] += 1
        
        for i in range(len(freq)):
            if freq[i] % 2 != 0:
                return chr(ord('a') + i)

