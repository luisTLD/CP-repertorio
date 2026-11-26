# CSES 1133 - Tree Distances II
# https://cses.fi/problemset/task/1133
import sys

def dfs_ordem(adj, s):
    pai = [-1] * len(adj); vis = [False] * len(adj); ordem = []; st = [s]; vis[s] = True
    while st:
        u = st.pop(); ordem.append(u)
        for v in adj[u]:
            if not vis[v]:
                vis[v] = True; pai[v] = u; st.append(v)
    return ordem, pai

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = ni(), ni()
        adj[u].append(v)
        adj[v].append(u)

    ordem, pai = dfs_ordem(adj, 1)
    sz = [1] * (n + 1)
    for u in reversed(ordem):
        if pai[u] != -1:
            sz[pai[u]] += sz[u]

    ans = [0] * (n + 1)
    ans_r = 0
    for u in ordem:
        if pai[u] != -1:
            ans[u] = ans[pai[u]] + 1
            ans_r += ans[u]
    ans = [0] * (n + 1)
    ans[1] = ans_r

    for u in ordem:
        if pai[u] != -1:
            ans[u] = ans[pai[u]] + (n - sz[u]) - sz[u]

    out.append(" ".join(map(str, ans[1:])))
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
