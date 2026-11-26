# CSES 1667 - Message Route
# https://cses.fi/problemset/task/1667
import sys
from collections import deque

def main():
    out = []

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n = ni()
    m = ni()

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a = ni()
        b = ni()
        graph[a].append(b)
        graph[b].append(a)

    parent = [-1] * (n + 1)
    parent[1] = 0

    q = deque([1])

    while q:
        u = q.popleft()

        if u == n:
            break

        for v in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                q.append(v)

    if parent[n] == -1:
        out.append("IMPOSSIBLE")
    else:
        path = []
        cur = n

        while cur != 0:
            path.append(cur)
            cur = parent[cur]

        path.reverse()

        out.append(len(path))
        out.append(" ".join(map(str, path)))

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
