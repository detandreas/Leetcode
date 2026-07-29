#class Solution:
#    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         """"Brute force method.""
#
#        def isAnagram(s: str, t: str) -> bool:
#            freq = [0] * 26
#
#            for c in s:
#                index = ord(c) - ord('a')
#                freq[index] += 1
#            for c in t:
#                index = ord(c) - ord('a')
#                freq[index] -= 1
#
#            return all(f == 0 for f in freq)
#        
#        skip = [False] * len(strs)
#        grouped = []
#        for i in range(len(strs)):
#
#            if skip[i]:
#                continue
#
#            s = strs[i]
#            grouped.append([s])
#
#            for j in range(i + 1, len(strs)):
#
#                if skip[j]:
#                    continue
#
#                t = strs[j]
#                if isAnagram(s, t):
#                    skip[j] = True
#                    grouped[-1].append(t)
#
#        return grouped
#
#strs = ["eat","tea","tan","ate","nat","bat"]
#s2 = [""]
#s3 = ["a"]
#sol = Solution()
#sol.groupAnagrams(s3)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Use freq table as a key to group elements.
        A list is not hashable and thus cannot be use as a key in a dict,
        so we transform it to a tuple first.
        """

        groups = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                freq[index] += 1
            key = tuple(freq)
            groups[key].append(s)

        return list(groups.values())
            


strs = ["eat","tea","tan","ate","nat","bat"]
s2 = [""]
s3 = ["a"]
sol = Solution()
print(sol.groupAnagrams(s3))
