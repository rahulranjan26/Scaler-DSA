class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        for i in range(len(A)):
            A[i] = list(A[i])
        if self.sudokuSolver(A, 0, 0, []):
            for i in range(len(A)):
                A[i] = ''.join(A[i])
        return A

    def sudokuSolver(self, board, i, j, res):
        if i == len(board):
            # res.append(board[:])
            return True

        new_row = 0
        new_col = 0
        if j == len(board) - 1:
            new_row = i + 1
            new_col = 0
        else:
            new_row = i
            new_col = j + 1

        if board[i][j] != '.':
            return self.sudokuSolver(board, new_row, new_col, res)
        else:
            for val in range(1, 10):
                if self.isValid(board, i, j, str(val)):
                    board[i][j] = str(val)
                    if self.sudokuSolver(board, new_row, new_col, res):
                        return True
                    board[i][j] = '.'
            return False

    def isValid(self, board, x, y, val):
        for i in range(0, 9):
            if board[i][y] == val:
                return False
        for j in range(0, 9):
            if board[x][j] == val:
                return False

        baseRow = 3 * (x // 3)
        baseCol = 3 * (y // 3)
        for i in range(0, 3):
            for j in range(0, 3):
                if board[baseRow + i][baseCol + j] == val:
                    return False

        return True
