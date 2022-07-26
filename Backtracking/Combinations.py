# TLE
import time
def combine(A, B):
    if A == 1 and B == 1:
        return [1]
    if A < B:
        return []
    if B==1:
        return A
    ans = set()
    ssf = ''
    visited = [False] * (A + 1)
    res = []
    start  = time.time()
    solver(A, B, ans, res, visited, '', [])
    print(time.time()-start)
    return res


def solver(A, B, ans, res, visited, ssf, asf):
    if len(asf) == B:
        temp = ''.join([str(x) for x in sorted(asf)])
        if temp not in ans:
            ans.add(temp)
            res.append(asf)
        return
    for i in range(1, A + 1):
        if visited[i] == False:
            visited[i] = True
            solver(A, B, ans, res, visited, ssf, asf + [i])
            visited[i] = False


print(combine(10, 8))

# Official:
