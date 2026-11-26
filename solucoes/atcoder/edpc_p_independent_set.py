# AtCoder EDPC P - Independent Set
# https://atcoder.jp/contests/dp/tasks/dp_p
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
    MOD = 10**9 + 7
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    t = ni()
    adj = [[] for _ in range(t + 1)]
    for _ in range(t - 1):
        u, v = ni(), ni()
        adj[u].append(v)
        adj[v].append(u)

    d = {}
    o, p = dfs_ordem(adj, 1)
    o.reverse()
    for i in range(len(o)):
        u, pi = o[i], p[o[i]]
        if u not in d: d[u] = [1, 1]
        if pi not in d: d[pi] = [1, 1]
        if pi != -1:
            d[pi][1] *= d[u][0] % MOD
            d[pi][0] *= (d[u][0] + d[u][1]) % MOD

    out.append((d[1][0] + d[1][1]) % MOD)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
