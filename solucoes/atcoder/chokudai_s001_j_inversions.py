# Chokudai 001 J - 転倒数
# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j
import sys

def main():
    out = []

    class Fenwick:
        def __init__(s, n, a=None):
            s.n = n; s.t = [0] * (n + 1)
            if a:
                for i in range(1, n + 1):
                    s.t[i] += a[i - 1]
                    j = i + (i & -i)
                    if j <= n: s.t[j] += s.t[i]
        def update(s, i, v):
            while i <= s.n:
                s.t[i] += v; i += i & -i
        def prefixo(s, i):
            r = 0
            while i > 0:
                r += s.t[i]; i -= i & -i
            return r
        def query(s, l, r):
            return s.prefixo(r) - s.prefixo(l - 1)

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n = ni()
    a = [ni() for _ in range(n)]
    f = Fenwick(n)
    ans = 0
    for ai in a:
        ans += f.query(ai, n)
        f.update(ai, 1)

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
