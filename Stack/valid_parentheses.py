class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        hashmap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif len(stack) == 0:
                return False
            else:
                if hashmap[ch] != stack.pop():
                    return False 
        return len(stack) == 0