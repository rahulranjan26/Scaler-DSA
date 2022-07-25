def subsetsWithDup(A):
    A.sort()
    ans = set()
    solve(A, ans, 0, [])
    return list(ans)


def solve(A, ans, idx, ssf):
    if idx == len(A):
        if len(ssf) > 0:
            ans.add(ssf)
        return
    solve(A, ans, idx + 1, ssf + [A[idx]])
    solve(A, ans, idx + 1, ssf)
