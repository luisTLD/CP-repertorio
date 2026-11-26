# AtCoder EDPC O - Matching
# https://atcoder.jp/contests/dp/tasks/dp_o
import sys

def main():
    MOD = 10**9 + 7
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()
    pairs = [[-1] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            mj = ni()
            if mj == 1:
                pairs[i].append(j)

    dp = [0] * ((2**n) + 1)
    dp[0] = 1

    c_actual = {0}
    for i in range(1, n + 1):
        c_new = set()
        for ci_actual in c_actual:
            for m in pairs[i][1:]:
                m_mask = 1 << (m - 1)
                if ci_actual & m_mask == 0:
                    ci_new = ci_actual | m_mask
                    dp[ci_new] = (dp[ci_new] + dp[ci_actual]) % MOD
                    c_new.add(ci_new)
        c_actual = c_new

    out.append(dp[(1 << n) - 1])
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
