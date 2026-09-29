class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        O(mn) time complexity.
        O(m + n) space complexity.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in rows:
            matrix[i][:] = [0] * n

        for j in cols:
            for i in range(m):
                matrix[i][j] = 0

class Neetcode:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        O(mn) time complexity.
        O(1) space complexity.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        first_row_zero = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0

        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0



s = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(matrix)