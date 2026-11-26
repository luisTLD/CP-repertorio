# AtCoder ABC177 D - Friends
# https://atcoder.jp/contests/abc177/tasks/abc177_d
import sys

def main():
    out = []

    class DSU:
        def __init__(s, n):
            s.p = list(range(n)); s.sz = [1] * n
        def find(s, x):
            r = x
            while s.p[r] != r: r = s.p[r]
            while s.p[x] != r: s.p[x], x = r, s.p[x]
            return r
        def union(s, a, b):
            a, b = s.find(a), s.find(b)
            if a == b: return False
            if s.sz[a] < s.sz[b]: a, b = b, a
            s.p[b] = a; s.sz[a] += s.sz[b]
            return True

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n, m = ni(), ni()

    d = DSU(n + 1)
    for _ in range(m):
        a, b = ni(), ni()
        d.union(a, b)

    out.append(max(d.sz))
    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
