from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        s_hashmap, t_hashmap = defaultdict(list), defaultdict(list)
        for i in range(n):
            s_hashmap[s[i]].append(i)
            t_hashmap[t[i]].append(i)

        for v_s, v_t in zip(s_hashmap.values(), t_hashmap.values()):
            if v_s != v_t:
                return False

        return True

class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mapping = {}
        used = set()
        for c1, c2 in zip(s, t):
            if c1 in mapping:
                if mapping[c1] != c2: return False
            elif c2 in used:
                return False
            else:
                mapping[c1] = c2
                used.add(c2)

        return True

class Solution3:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

class Neetcode:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):

            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True




s = "egg"
t = "add"
sol = Solution()
sol.isIsomorphic(s,t)