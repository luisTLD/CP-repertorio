# AtCoder ABC314 D - LOWER
# https://atcoder.jp/contests/abc314/tasks/abc314_d
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    ns = lambda: next(it).decode()
    out = []

    n = ni()
    ans = list(ns())
    q = ni()
    txc = [[ns(), ns(), ns()] for _ in range(q)]

    s = set()
    converted = False
    to_upper = False
    for t, x, c in txc[::-1]:
        t = int(t)
        x = int(x)

        if converted is False and (t in [2, 3]):
            to_upper = True if t == 3 else False
            converted = True
            continue

        if t == 1:
            if x in s:
                continue

            if converted is False:
                ans[x - 1] = c
                s.add(x)
            else:
                c = c.upper() if to_upper is True else c.lower()
                ans[x - 1] = c
                s.add(x)

    for i, c in enumerate(ans):
        if converted is False:
            continue
        if i + 1 in s:
            continue
        ans[i] = c.upper() if to_upper is True else c.lower()

    out.append("".join(ans))
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
