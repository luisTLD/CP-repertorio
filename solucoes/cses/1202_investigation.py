# CSES 1202 - Investigation
# https://cses.fi/problemset/task/1202
import sys
import heapq

INF = float('inf')
def dijkstra(adj, s):
    d = [INF] * len(adj); d[s] = 0; h = [(0, s)]
    while h:
        du, u = heapq.heappop(h)
        if du > d[u]: continue
        for v, w in adj[u]:
            if du + w < d[v]:
                d[v] = du + w; heapq.heappush(h, (d[v], v))
    return d

def main():
    MOD = 10**9 + 7
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n, m = ni(), ni()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = ni(), ni(), ni()
        adj[u].append((v, w))

    d = dijkstra(adj, 1)
    idx = sorted(range(1, len(d)), key=lambda i: d[i])

    info = [[d[i], 0, float('inf'), -float('inf')] for i in range(len(d))]
    info[1] = [0, 1, 0, 0]
    for u in idx:
        for v, c in adj[u]:
            if d[v] == d[u] + c:
                info[v][0] = d[v]
                info[v][1] = (info[v][1] + info[u][1]) % MOD
                info[v][2] = min(info[v][2], info[u][2] + 1)
                info[v][3] = max(info[v][3], info[u][3] + 1)

    out.append(" ".join(map(str, info[n])))
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
