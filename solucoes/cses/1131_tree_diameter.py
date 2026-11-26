# CSES 1131 - Tree Diameter
# https://cses.fi/problemset/task/1131
import sys
from collections import deque

def main():
    out = []

    def bfs(adj, s):
        d = [-1] * len(adj); d[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[v] == -1:
                    d[v] = d[u] + 1; q.append(v)
        return d

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n = ni()
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = ni(), ni()
        adj[u].append(v)
        adj[v].append(u)

    d = bfs(adj, 1)
    ans = max(enumerate(bfs(adj, max(enumerate(bfs(adj, 1)), key=lambda x: x[1])[0])), key=lambda x: x[1])[1]

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
