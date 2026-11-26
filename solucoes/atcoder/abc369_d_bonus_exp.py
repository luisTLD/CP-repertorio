# AtCoder ABC369 D - Bonus EXP
# https://atcoder.jp/contests/abc369/tasks/abc369_d
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()
    a = [ni() for _ in range(n)]

    dp = [[0, 0] for _ in range(n + 1)]
    dp[1] = [a[0], 0]
    for i in range(2, n + 1):
        dp[i][0] = max(dp[i - 1][1] + a[i - 1], dp[i - 1][0])
        dp[i][1] = max(dp[i - 1][0] + (a[i - 1] * 2), dp[i - 1][1])

    out.append(max(dp[n][0], dp[n][1]))
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
