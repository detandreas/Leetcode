class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Better version of my solution.No encoding of geometry in evolving state.
        Index mapping (i, j) -> (j, n-1-i)
        O(n^2) time complexity
        O(1) space complexity
        """

        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                tmp = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = tmp
            l += 1
            r -= 1

class Solution2:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Better version of my solution.No encoding of geometry in evolving state.
        Index mapping (i, j) -> (j, n-1-i)
        O(n^2) time complexity
        O(1) space complexity
        """

        n = len(matrix)
        l, r = 0, n - 1
        while l < r:
            for k in range(r - l):
                si, sj = l, l + k
                curr = matrix[si][sj]
                i, j = sj, n - 1 - si
                for _ in range(4):
                    curr, matrix[i][j] = matrix[i][j], curr
                    i, j = j, n - 1 - i
            l += 1
            r -= 1

from math import ceil

class   dumb_solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Idk what the fuck is this dumb solution.
        """
        moves = {
            0: [1, -1],
            1: [-1, -1],
            2: [-1, 1],
            3: [1, 1]
        }

        l, r = 0, len(matrix) - 1
        for row in range(0, ceil(len(matrix) / 2) + 1):
            shift = r - l
            directions = [[0, shift], [shift, 0], [0, -shift], [-shift, 0]]
            for col in range(l, r):
                curr_element, matrix[row][col] = matrix[row][col], None
                i_shift = row
                j_shift = col
                m = 0
                print(f"we start {i_shift=}, {j_shift=}, {curr_element=}")
                while curr_element is not None:
                    d = directions[m]

                    # update position
                    i_shift += d[0]
                    j_shift += d[1]

                    # update directions
                    d[0] += moves[m][0]
                    d[1] += moves[m][1]

                    # next move
                    m = (m + 1) % 4
                    print(f"{i_shift=}, {j_shift=}, {curr_element=}")
                    curr_element, matrix[i_shift][j_shift] = matrix[i_shift][j_shift], curr_element
                print(f"we stopped {i_shift=}, {j_shift=}, {curr_element=}")

            l += 1
            r -= 1

s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(matrix)
