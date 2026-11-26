# AtCoder ABC345 C - One Time Swap
# https://atcoder.jp/contests/abc345/tasks/abc345_c
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ns = lambda: next(it).decode()
    out = []

    s = list(ns())

    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1

    rep = False
    ans = 0
    for v in d.values():
        if v > 1:
            rep = True
        ans += (v * (len(s) - v))

    ans //= 2
    if rep is True:
        ans += 1

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
