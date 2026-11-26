# CSES 1141 - Playlist
# https://cses.fi/problemset/task/1141
import sys

def main():
    out = []

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n = ni()
    a = [ni() for _ in range(n)]

    s = 0
    ans = 0
    d = {}
    for i in range(n):
        if a[i] in d and d[a[i]] >= s:
            ans = max(ans, i - s)
            s = d[a[i]] + 1
        d[a[i]] = i
    ans = max(ans, n - s)

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
