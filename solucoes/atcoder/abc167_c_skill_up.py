# AtCoder ABC167 C - Skill Up
# https://atcoder.jp/contests/abc167/tasks/abc167_c
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n, m, x = ni(), ni(), ni()
    books = []
    for _ in range(n):
        info = [ni() for _ in range(m + 1)]
        books.append([info[0], info[1:]])

    ans = float('inf')
    stack = []
    stack.append([0, 0, [0] * m])
    while stack:
        i, p, s = stack.pop()
        if i == n:
            p = float('inf') if min(s) < x else p
            ans = min(ans, p)
            continue

        stack.append([i + 1, p, s.copy()])
        bs = books[i][1]
        si = [s[i] + bs[i] for i in range(m)]
        if min(si) >= x:
            ans = min(ans, p + books[i][0])
        else:
            stack.append([i + 1, p + books[i][0], si])

    out.append(ans if ans != float('inf') else -1)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
