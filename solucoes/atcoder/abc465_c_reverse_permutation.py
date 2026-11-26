# AtCoder ABC465 C - Reverse Permutation
# https://atcoder.jp/contests/abc465/tasks/abc465_c
import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    ns = lambda: next(it).decode()
    out = []

    n = ni()
    s = list(ns())
    a = list(range(1, n + 1))

    d = deque()
    d.append(a[0])
    flag = True
    for i in range(1, n):
        if s[i] == 'x':
            if flag is False:
                d.append(a[i])
            else:
                d.appendleft(a[i])
            continue

        flag = not flag
        if flag is True:
            d.append(a[i])
        else:
            d.appendleft(a[i])

    if flag is False:
        out.append(' '.join(map(str, d)))
    else:
        out.append(' '.join(map(str, reversed(d))))

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
