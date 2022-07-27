def solveNQueens(A):
    board = [['.'] * A for _ in range(A)]
    ans = []
    solver(A, board, ans, -1)
    return ans


def solver(A, chess, ans, llb):
    if A == 0:
        temp=[]
        for row in chess:
            temp.append(row[:])
        ans.append(temp)
        return
    for i in range(llb + 1, len(chess) ** 2):
        row = i // len(chess)
        col = i % len(chess)
        if chess[row][col] == '.' and isSafe(chess, row, col):
            chess[row][col] = 'q'
            solver(A - 1, chess, ans, row * len(chess) + col)
            chess[row][col] = '.'


def isSafe(chess, row, col):
    i = row - 1

    while i >= 0:
        if chess[i][col] == 'q':
            return False
        i = i - 1

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if chess[i][j] == 'q':
            return False
        i = i - 1
        j = j - 1
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(chess):
        if chess[i][j] == 'q':
            return False
        i = i - 1
        j = j + 1
    i = row
    j = col - 1
    while j >= 0:

        if chess[i][j] == 'q':
            return False
        j = j - 1

    return True


# print(solveNQueens(4))
def NqueensBranchAndBound(n):
    cols = [False] * n
    leftDiag = [False] * (2 * n - 1)
    rightDiag = [False] * (2 * n - 1)
    row = 0
    solve(row, cols, leftDiag, rightDiag, '')


def solve(row, cols, leftDiag, rightDiag, ssf):
    if row == len(cols):
        print(ssf.split(' '))
        return
    for col in range(len(cols)):
        if cols[col] == False and leftDiag[row - col + len(cols) - 1] == False and rightDiag[row + col] == False:
            cols[col] = True
            leftDiag[row - col + len(cols) - 1] = True
            rightDiag[row + col] = True
            solve(row + 1, cols, leftDiag, rightDiag, ssf + str(row) + '-' + str(col)+' ')
            cols[col] = False
            leftDiag[row - col + len(cols) - 1] = False
            rightDiag[row + col] = False


NqueensBranchAndBound(4)

