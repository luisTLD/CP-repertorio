# CSES 1681 - Game Routes
# https://cses.fi/problemset/task/1681
import sys
from collections import deque

def kahn(adj, ini=0):
    n = len(adj); g = [0] * n
    for u in range(ini, n):
        for v in adj[u]: g[v] += 1
    q = deque(i for i in range(ini, n) if g[i] == 0); o = []
    while q:
        u = q.popleft(); o.append(u)
        for v in adj[u]:
            g[v] -= 1
            if g[v] == 0: q.append(v)
    return o

def main():
    MOD = 10**9 + 7
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n, m = ni(), ni()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = ni(), ni()
        adj[u].append(v)

    ordem = kahn(adj, 1)
    dp = [0] * (len(adj))
    dp[len(adj) - 1] = 1
    for u in reversed(ordem):
        for v in adj[u]:
            dp[u] = (dp[u] + dp[v]) % MOD

    out.append(dp[1])
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
