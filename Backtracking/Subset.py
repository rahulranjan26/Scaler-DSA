# Sol : 1
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()

    ans = []
    idx = 0

    self.solver(A, ans, idx, [])
    return sorted(ans)


def solver(self, A, ans, idx, ssf):
    if idx == len(A):
        ans.append(ssf)
        return
    self.solver(A, ans, idx + 1, ssf + [A[idx]])
    self.solver(A, ans, idx + 1, ssf)

# Official
