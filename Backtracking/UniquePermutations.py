class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        seen = [False] * len(A)

        ans = []
        res = set()
        self.solver(A, seen, ans, [], '', res)
        return ans


def solver(self, A, seen, ans, ssf, sf, res):
    if len(ssf) == len(A):
        if sf not in res:
            ans.append(ssf[:])
            res.add(sf)
        return
    for i in range(len(A)):
        if not seen[i]:
            seen[i] = True
            self.solver(A, seen, ans, ssf + [A[i]], sf + str(A[i]), res)
            seen[i] = False
