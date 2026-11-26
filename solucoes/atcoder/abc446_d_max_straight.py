# AtCoder ABC446 D - Max Straight
# https://atcoder.jp/contests/abc446/tasks/abc446_d
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()
    a = [ni() for _ in range(n)]

    dp = {}
    for ai in a:
        dp[ai] = dp.get(ai - 1, 0) + 1

    out.append(max(dp.values()))
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
