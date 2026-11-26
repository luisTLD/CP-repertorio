# AtCoder ABC385 C - Illuminate Buildings
# https://atcoder.jp/contests/abc385/tasks/abc385_c
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()
    h = [ni() for _ in range(n)]
    ans = 1
    for i in range(n):
        for j in range(i + 1, n):
            count = 1
            for k in range(i + j, n, j):
                if h[k - j] == h[k]:
                    count += 1
                else:
                    ans = max(ans, count)
                    count = 1
            ans = max(ans, count)

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
