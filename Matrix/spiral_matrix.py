class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        move order:
        right -> down -> left -> up

        moves = {right: 0, down: 1, left: 2, up: 3}

        next_move = (move + 1) % 4

        O(m * n) time complexity
        O(m * n) space complexity
        """

        m = len(matrix)
        n = len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        i = j = 0
        move = 0
        res: list[int] = []

        while len(res) < m * n:

            if not visited[i][j]:
                visited[i][j] = True
                res.append(matrix[i][j])

            if move == 0:
                if j + 1 < n and not visited[i][j+1]:
                    j += 1
                    continue
                move = (move + 1) % 4
            elif move == 1:
                if i + 1 < m and not visited[i+1][j]:
                    i += 1
                    continue
                move = (move + 1) % 4
            elif move == 2:
                if j - 1 > -1 and not visited[i][j-1]:
                    j -= 1
                    continue
                move = (move + 1) % 4
            else:
                if i - 1 > -1 and not visited[i-1][j]:
                    i -= 1
                    continue
                move = (move + 1) % 4

        return res

class Solution2:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        Using direction vectors to avoid if-else statements
        """
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        i = j = d = 0
        res = []

        for _ in range(m * n):
            res.append(matrix[i][j])
            visited[i][j] = True
            ni, nj = i + dirs[d][0], j + dirs[d][1]
            if not (0 <= ni < m and 0 <= nj < n) or visited[ni][nj]:
                d = (d + 1) % 4
                ni, nj = i + dirs[d][0], j + dirs[d][1]
            i, j = ni, nj

        return res

class Neetcode:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """
        Shrinking boundaries
        O(m * n) time complexity
        O(1) space complexity
        """
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []

        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res