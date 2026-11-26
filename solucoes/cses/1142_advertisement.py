# CSES 1142 - Advertisement
# https://cses.fi/problemset/task/1142
import sys

def main():
    out = []

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n = ni()
    a = [ni() for _ in range(n)]

    s = []
    l = [-1] * n
    r = [-1] * n
    for i in range(n):
        while s and a[i] <= a[s[len(s) - 1]]:
            s.pop()
        if s: l[i] = s[len(s) - 1]
        s.append(i)

    s = []
    for i in range(n - 1, -1, -1):
        while s and a[i] <= a[s[len(s) - 1]]:
            s.pop()
        if s: r[i] = s[len(s) - 1]
        s.append(i)

    ans = 0
    for i in range(n):
        li, ri = l[i], r[i]
        if ri == -1: ri = n
        ans = max(ans, a[i] * (ri - li - 1))

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
