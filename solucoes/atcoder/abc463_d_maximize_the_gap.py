# AtCoder ABC463 D - Maximize the Gap
# https://atcoder.jp/contests/abc463/tasks/abc463_d
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n, k = ni(), ni()
    lr = [(ni(), ni()) for _ in range(n)]

    lr.sort(key=lambda x: x[1])
    ans = -1

    i = 1
    j = lr[n - 1][1] - lr[0][1]
    while i <= j:
        d = (i + j) // 2
        actual = lr[0]
        using = 1
        for lri in lr[1:]:
            if using >= k:
                break
            if lri[0] - actual[1] >= d:
                using += 1
                actual = lri
        if using >= k:
            ans = d
            i = d + 1
        else:
            j = d - 1

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
