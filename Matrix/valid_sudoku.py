import string

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        You can find the subgrid with the followin formula:
        subgrid = (i // 3) * 3 + (j // 3)
        """

        observed: dict[str, tuple[set, set, set]] = {digit: (set(), set(), set()) for digit in string.digits}

        for i, row in enumerate(board):
            for j, slot in enumerate(row):

                if not slot.isdigit(): continue

                # check row
                if i in observed[slot][0]: return False
                observed[slot][0].add(i)

                # check column
                if j in observed[slot][1]: return False
                observed[slot][1].add(j)

                # find subgrid
                if i <= 2: r_eligible = {0, 1, 2}
                elif i <= 5: r_eligible = {3, 4, 5}
                else: r_eligible = {6, 7, 8}

                if j <= 2: c_eligible = {0, 3, 6}
                elif j <= 5: c_eligible = {1, 4, 7}
                else: c_eligible = {2, 5, 8}

                subgrid = r_eligible.intersection(c_eligible).pop()

                # check subgrid
                if subgrid in observed[slot][2]: return False
                observed[slot][2].add(subgrid)


        return True

s = Solution()
board = \
[[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
print(s.isValidSudoku(board))

import string

class Solution2:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        observed: dict[str, tuple[set, set, set]] = {digit: (set(), set(), set()) for digit in string.digits}

        for i, row in enumerate(board):
            for j, slot in enumerate(row):

                if not slot.isdigit(): continue

                subgrid = (i // 3) * 3 + (j // 3)

                # check row
                if i in observed[slot][0]: return False
                observed[slot][0].add(i)

                # check column
                if j in observed[slot][1]: return False
                observed[slot][1].add(j)

                # check subgrid
                if subgrid in observed[slot][2]: return False
                observed[slot][2].add(subgrid)


        return True
