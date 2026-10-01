from collections import defaultdict

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors: dict[tuple, list[int]] = defaultdict(list)

        m, n  = len(board), len(board[0])
        for i in range(m):
            for j in range(n):

                # Κάθετα κάτω
                if i + 1 < m:
                    neighbors[(i, j)].append(board[i + 1][j])
                    neighbors[(i + 1, j)].append(board[i][j])

                # Οριζόντια δεξιά
                if j + 1 < n:
                    neighbors[(i, j)].append(board[i][j + 1])
                    neighbors[(i, j + 1)].append(board[i][j])

                # Διαγώνια κάτω αριστερά
                if i + 1 < m and j - 1 > -1:
                    neighbors[(i, j)].append(board[i + 1][j - 1])
                    neighbors[(i + 1, j - 1)].append(board[i][j])

                # Διαγώνια κάτω δεξιά
                if i + 1 < m and j + 1 < n:
                    neighbors[(i, j)].append(board[i + 1][j + 1])
                    neighbors[(i + 1, j + 1)].append(board[i][j])

        for i in range(m):
            for j in range(n):

                key = (i, j)
                live_neighbors = sum(neighbors[key])

                # alive cell
                if board[i][j] == 1:

                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 0

                    continue

                # dead cell
                if live_neighbors == 3:
                    board[i][j] = 1


class BitEncoding:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Imagine that each cell in the board contains 2 bits.
        Least significant bit is the current state and the Most significant bit is the next state.

        board = [
                [0,1,0],
                [0,0,1],
                [1,1,1],
                [0,0,0]]

        is initially this
        bit_board = [
                [00,01,00],
                [00,00,01],
                [01,01,01],
                [00,00,00]]

        We count the live neighbors of each cell and we encode the next state.
        live_neighbors += board[r][c] & 1 (counting technique).
        We change the next state only to 1 because every cell has initially next state 0.

        after first pass (next | current):
        [[00, 01, 00],
         [10, 00, 11],
         [01, 11, 11],
         [00, 10, 00]]

        After we finish with all the cells we remove the previous state (by shifting 1 bit to the right ).
        after >> 1:
        [[0, 0, 0],
         [1, 0, 1],
         [0, 1, 1],
         [0, 1, 0]]
        """

        m, n = len(board), len(board[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]

        for i  in range(m):
            for j in range(n):
                live_neighbors = 0
                for di, dj in dirs:
                    r, c = i + di, j + dj

                    if 0 <= r < m and 0 <= c < n:
                        live_neighbors += board[r][c] & 1

                alive = board[i][j] & 1
                if (alive and live_neighbors in (2, 3)) or (not alive and (live_neighbors == 3)):
                    board[i][j] |= 2 # board[i][j] = board[i][j] | 2    00 | 10 = 10    or  01 | 10 = 11

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1 # board[i][j] = board[i][j] >> 1


s = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(board)


