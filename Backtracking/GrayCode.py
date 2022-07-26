def grayCode(A):
    # ans = []
    ans = solver(A)
    ans = [int(x, 2) for x in ans]
    return ans


def solver(A):
    if A == 1:
        return ['0', '1']
    temp = solver(A - 1)
    ans = [x + '1' for x in temp] + [x + '0' for x in temp[::-1]]
    return ans


print(grayCode(3))

'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
There might be multiple gray code sequences possible for a given n.

Return any such sequence.
'''
