# CSES 1135 - Distance Queries
# https://cses.fi/problemset/task/1135
import sys

def main():
    out = []

    def dfs_ordem(adj, s):
        pai = [-1] * len(adj); vis = [False] * len(adj); ordem = []; st = [s]; vis[s] = True
        while st:
            u = st.pop(); ordem.append(u)
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True; pai[v] = u; st.append(v)
        return ordem, pai

    def profundidades(ordem, pai):
        dep = [0] * len(pai)
        for u in ordem:
            if pai[u] != -1: dep[u] = dep[pai[u]] + 1
        return dep

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n, m = ni(), ni()
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = ni(), ni()
        adj[u].append(v)
        adj[v].append(u)

    ordem, pai = dfs_ordem(adj, 1)
    dep = profundidades(ordem, pai)

    deepest = max(dep)
    if deepest == 0: deepest = 1
    bl = [[0] * (n + 1) for _ in range(deepest.bit_length())]

    for j in range(1, n + 1):
        bl[0][j] = pai[j]
        if bl[0][j] == -1: bl[0][j] = 0

    for i in range(1, deepest.bit_length()):
        for j in range(1, n + 1):
            bl[i][j] = bl[i-1][bl[i-1][j]]

    for _ in range(m):
        a, b = ni(), ni()
        ai, bi = a, b

        if dep[a] != dep[b]:
            if dep[a] < dep[b]: a, b = b, a
            dif = dep[a] - dep[b]
            jump = dif.bit_length() - 1
            while dif > 0:
                a = bl[jump][a]
                dif -= 1 << jump
                jump = dif.bit_length() - 1

        lca = a
        if a != b:
            jump = dep[a].bit_length() - 1
            while jump >= 0:
                if bl[jump][a] != bl[jump][b]:
                    a, b = bl[jump][a], bl[jump][b]
                jump -= 1
            lca = bl[0][a]
        out.append(dep[ai] + dep[bi] - 2*dep[lca])

    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
