class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        grid = [[] for _ in range(numRows)]
        index = 0
        step = None
        for ch in s:
            if index == 0:
                step = 1
            
            if index == numRows - 1:
                step = -1
            
            grid[index].append(ch)
            index += step
        
        print(grid)
        out = []
        for l in grid:
            out.extend(l)
        
        return "".join(out)

sol = Solution()
s = "PAYPALISHIRING"
s2 = "ABC"
print(sol.convert(s2, 1))