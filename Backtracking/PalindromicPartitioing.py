def partition(A):
    ans = []
    solver(A, ans, [])
    return ans


def solver(A, ans, ssf):
    if len(A) == 0:
        ans.append(ssf[:])
        return
    for i in range(len(A)):
        temp = A[:i + 1]
        if temp == temp[::-1]:
            ros = A[i + 1:]
            solver(ros, ans, ssf + [temp])


print(partition('abcdefedcba'))
