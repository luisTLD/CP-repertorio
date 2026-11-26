# ALPC B - Fenwick Tree
# https://atcoder.jp/contests/practice2/tasks/practice2_b
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

    n, q = ni(), ni()
    f = Fenwick(n)
    for i in range(1, n + 1):
        f.update(i, ni())

    for _ in range(q):
        qi = ni()
        if qi == 0:
            p, x = ni(), ni()
            f.update(p + 1, x)
        else:
            l, r = ni(), ni()
            out.append(f.query(l + 1, r))

    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
