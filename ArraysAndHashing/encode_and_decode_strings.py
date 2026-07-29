class Solution:
    
    def __init__(self):
        self.test = [0]

    def encode(self, strs: list[str]) -> str:

        self.test *= len(strs)
        for i in range(len(strs)):
            self.test[i] = len(strs[i])
        
        return "".join(strs)
    
    def decode(self, s: str) -> list[str]:
        out = []
        lower = 0
        for upper in self.test:
            out.append(s[lower : upper + lower])
            print(f"{lower=}, {upper + lower=}")
            lower += upper
        return out