# AtCoder ABC362 C - Sum = 0
# https://atcoder.jp/contests/abc362/tasks/abc362_c
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()

    lr = []
    for _ in range(n):
        l, r = ni(), ni()
        lr.append((l, r))

    tl = 0
    tr = 0

    for l, r in lr:
        tl += l
        tr += r

    if not (tl <= 0 <= tr):
        out.append("No")
    else:
        out.append("Yes")

        x = [l for l, r in lr]
        need = -tl

        for i in range(n):
            l, r = lr[i]

            add = min(need, r - l)
            x[i] += add
            need -= add

        out.append(" ".join(map(str, x)))

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
