def generate(n):
    ans = set()
    ssf = ''
    ssof = 0
    open = n
    close = n

    solve(ans, ssf, ssof, open, close)
    return ans


def solve(ans, ssf, ssof, open, close):
    if open == 0 and close == 0:
        if ssof==0:
            ans.add(ssf)
        return
    if len(ssf)==0:
        solve(ans, ssf + '(', ssof + 1, open - 1, close)
    if open > 0:
        solve(ans, ssf + '(', ssof + 1, open - 1, close)
    if close > 0:
        if ssof > 0:
            solve(ans, ssf + ')', ssof - 1, open, close - 1)


print(generate(3))
