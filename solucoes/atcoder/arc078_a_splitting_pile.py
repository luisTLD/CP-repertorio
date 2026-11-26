# AtCoder ARC078 C / ABC067 C - Splitting Pile
# https://atcoder.jp/contests/abc067/tasks/arc078_a
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()
    a = [ni() for _ in range(n)]

    tr = sum(a)
    tl = 0
    ans = float("inf")

    for i in range(len(a) - 1):
        tl += a[i]
        tr -= a[i]
        diff = abs(tl - tr)
        ans = min(ans, diff)

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
