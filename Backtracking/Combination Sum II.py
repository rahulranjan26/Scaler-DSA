# official :


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        res = []

        def backtrack(idx=0, currSum=0, currList=[]):
            if currSum > B:
                return
            elif currSum == B:
                res.append(currList)
                return
            else:
                for i in range(idx, len(A)):
                    if i != idx and A[i] == A[i - 1]:
                        continue
                    backtrack(i + 1, currSum + A[i], currList + [A[i]])

        backtrack()
        return sorted(res)

    # https://www.interviewbit.com/problems/combination-sum/ (similar)
    # https://leetcode.com/problems/combination-sum-ii/ (leetcode solution)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        ans = set()
        res = []
        idx = 0
        self.solver(A, B, ans, res, [], idx, '')
        return sorted(res)

    def solver(self, A, B, ans, res, ssf, idx, st):
        if B == 0:
            if ssf not in res:
                # ans.add(st)
                res.append(ssf)
                return
        if idx == len(A) or B < 0:
            return
        self.solver(A, B - A[idx], ans, res, ssf + [A[idx]], idx + 1, st + str(A[idx]) + '#')
        self.solver(A, B, ans, res, ssf, idx + 1, st + '#')

