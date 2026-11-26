# AtCoder ABC256 D - Union of Interval
# https://atcoder.jp/contests/abc256/tasks/abc256_d
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()
    lr = [[ni(), ni()] for _ in range(n)]

    ans = []
    lr.sort(key=lambda lr: (lr[0], -lr[1]))
    start = lr[0][0]
    end = lr[0][1]
    for lri in lr:
        if lri[0] <= end and lri[1] > end:
            end = lri[1]
        if lri[0] > end:
            ans.append([start, end])
            start = lri[0]
            end = lri[1]
    ans.append([start, end])

    for ansi in ans:
        out.append(f"{ansi[0]} {ansi[1]}")

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
