class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True
        
        cp = s
        cp.casefold()
        cp = ''.join(filter(str.isalnum,  cp))
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True