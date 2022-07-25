'''Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
NOTE

No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.

Example : next_permutations in C++ / itertools.permutations in python.

If you do, we will disqualify your submission retroactively and give you penalty points.'''


# Sol:1
class Solution:
    # @param A : list of integers
    # @return a list of  integers
    def permute(self, A):
        ans = []

        visited = [False] * len(A)
        self.solve(A, ans, visited, [])
        return ans


def solve(self, A, ans, visited, ssf):
    if len(ssf) == len(A):
        ans.append(ssf[:])
        return
    for i in range(len(A)):
        if visited[i] == False:
            visited[i] = True
            self.solve(A, ans, visited, ssf + [A[i]])
            visited[i] = False

# Official Sol:
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if(len(A) == 1):
            return [A]
        res = []
        for i in range(len(A)):
            nxt = self.permute(A[:i] + A[i+1:])
            for j in nxt:
                res.append([A[i]] + j)
        return res