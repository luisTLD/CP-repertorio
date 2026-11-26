# CSES 1675 - Road Reparation
# https://cses.fi/problemset/task/1675
import sys
import heapq

def main():
    out = []

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n, m = ni(), ni()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = ni(), ni(), ni()
        adj[u].append((v, w))
        adj[v].append((u, w))

    visited = set()
    visited.add(1)
    h = []
    heapq.heapify(h)
    for v, w in adj[1]:
        heapq.heappush(h, (w, v))

    ans = 0
    while h:
        w, v = heapq.heappop(h)
        if v not in visited:
            ans += w
            visited.add(v)
            for vi, w in adj[v]:
                heapq.heappush(h, (w, vi))

    if len(visited) < n: ans = "IMPOSSIBLE"
    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
