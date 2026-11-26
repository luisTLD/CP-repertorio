# AtCoder ABC054 B - Template Matching
# https://atcoder.jp/contests/abc054/tasks/abc054_b
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    ns = lambda: next(it).decode()
    out = []

    n, m = ni(), ni()
    a = [list(ns()) for _ in range(n)]
    b = [list(ns()) for _ in range(m)]

    verify = False
    if m <= n:
        for i in range(n):
            if verify is True:
                break
            for j in range(n):
                if verify is True:
                    break
                if a[i][j] == b[0][0]:
                    verify = True
                    for k in range(m):
                        if verify is False:
                            break
                        for l in range(m):
                            if i + k >= n or j + l >= n:
                                verify = False
                                break
                            if a[i + k][j + l] != b[k][l]:
                                verify = False
                                break

    out.append("Yes" if verify is True else "No")
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
