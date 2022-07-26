def letterCombinations(A):
    mapLetter = {
        # '1':['1'],
        # '0':['0'],
        '2': list('abc'),
        '3': list('def'),
        '4': list('ghi'),
        '5': list('jkl'),
        '6': list('mno'),
        '7': list('pqrs'),
        '8': list('tuv'),
        '9': list('wxyz')

    }

    ans = []
    return solve(A, mapLetter)
    # return ans


def solve(A, mapLetter):
    if len(A) == 1:
        return mapLetter[A[0]]
    temp = A[0]
    rest = A[1:]
    res = solve(rest, mapLetter)
    ans = []
    for pre in mapLetter[temp]:
        for el in res:
            ans.append(pre + el)
    return ans

print(letterCombinations('23'))