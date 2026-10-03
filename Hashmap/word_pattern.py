class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        mapPS: dict[str, str] = {}
        mapSP: dict[str, str] = {}

        for p, w in zip(pattern, words):

            if ((p in mapPS and mapPS[p] != w) or
                (w in mapSP and mapSP[w] != p)):
                return False

            mapPS[p] = w
            mapSP[w] = p

        return True