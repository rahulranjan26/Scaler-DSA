def combinationSum(A, B):
    ans = []
    A.sort()
    # res = []
    visited = [False] * len(A)
    solver(A, B, ans, [], visited, 0)
    return ans


def solver(A, B, ans, ssf, visited, idx):
    if B == 0:
        # if sorted(ssf) not in ans:
        ans.append(ssf[:])
        return
    if idx == len(A):
        return
        # if B < 0:
    #     return
    if B > 0:
        for i in range(idx, len(A)):
            solver(A, B - A[i], ans, ssf + [A[i]], visited, idx)
    else:
        for i in range(idx, len(A)):
            solver(A, B - A[i], ans, ssf + [A[i]], visited, idx + 1)


print(combinationSum([2, 3, 5, 7], 7))

# Official 1:
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        unique_sorted_A = sorted(list(set(A)))
        return get_combination_sum(unique_sorted_A, B)


def get_combination_sum(A, B):
    if B < 0:
        return list()
    if B == 0:
        return [[]]
    combinations = list()
    for index, a in enumerate(A):
        new_combs = get_combination_sum(A[index:], B - a)
        combinations += [[a] + x for x in new_combs]
    return combinations

# Official 2:
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, candidates, target):
        if not candidates:
            return
        if target == 0:
            self.result.append(self.currList[:])
            return
        if candidates[0] <= target:
            self.currList.append(candidates[0])
            self.solve(candidates, target - candidates[0])
            self.currList.pop()

        return self.solve(candidates[1:], target)

    def combinationSum(self, A, B):
        self.result = []
        self.currList = []
        A = list(dict.fromkeys(A))
        A.sort()
        self.solve(A, B)
        return self.result


