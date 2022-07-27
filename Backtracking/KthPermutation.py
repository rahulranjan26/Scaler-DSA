import math
def getPermutation(A, B):
    ans = []
    res = []
    visited = [False] * (A + 1)
    solver(A, B, res, ans, visited)
    return ans[B-1]


def solver(A, B, res, ans, visited):
    if len(res) == A:
        temp = ''.join(str(x) for x in res)
        ans.append(temp)
        return
    for i in range(1, A + 1):
        if visited[i] == False:
            visited[i] = True
            solver(A, B - 1, res + [i], ans, visited)
            visited[i] = False




print(getPermutation(5,48))


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, n, k):
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])
        return permutation