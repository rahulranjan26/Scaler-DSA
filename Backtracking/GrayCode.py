def grayCode(A):
    # ans = []
    ans = solver(A)
    ans = [int(x) for x in ans]


def solver(A):
    if A == 1:
        return ['0', '1']
    temp = solver(A - 1)
    ans = [x + '1' for x in temp] + [x + '0' for x in temp[::-1]]
    return ans

print(grayCode(3))