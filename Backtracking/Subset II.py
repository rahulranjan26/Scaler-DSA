# Sol:1
def subsetsWithDup(A):
    A.sort()
    ans = set()
    res=[]
    solve(A, ans, 0, [], '', res)
    return res


def solve(A, ans, idx, ssf, st, res):
    if idx == len(A):
        if st not in ans:
            ans.add(st)
            res.append(ssf)
        return
    solve(A, ans, idx + 1, ssf + [A[idx]], st + str(A[idx]) + '#',res)
    solve(A, ans, idx + 1, ssf, st + '',res)


print(subsetsWithDup([1, 2, 2]))

# Official
def subsetsWithDup(self, A):
    res = []

    def subset(result, cur, rest):
        if not rest:
            if cur not in result:
                result += [cur]
        else:
            subset(result, cur, rest[1:])
            subset(result, cur + [rest[0]], rest[1:])

    subset(res, [], sorted(A))

    return sorted(res)
