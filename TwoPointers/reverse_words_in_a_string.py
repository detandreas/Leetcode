class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        
        res = list()
        word = ""
        for ch in s:
            if ch == " ":
                if word != "":
                    res.insert(0, word)
                    word = ""
                else:
                    continue
            else:
                word += ch

        if word != "":
            res.insert(0, word)

        return " ".join(res)
    
from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        
        res = deque()
        start = -1
        i = 0
        while i < len(s):
            ch = s[i]
            if ch != " ":
                start = i
                while i < len(s) and s[i] != " ":
                    i += 1
                res.appendleft(s[start : i])
            i += 1 

        return " ".join(res)
                



sol = Solution()
s = "  hello world  "
s2 = "a good   example"
s3 = "the sky is blue"
print(sol.reverseWords(s3))
