import sys
from collections import deque, Counter, defaultdict
import heapq, bisect, math

INF = float('inf')


def rankear_grafo(g):
    rot = sorted(set(g) | {v for vs in g.values() for v in vs})
    id_ = {x: i for i, x in enumerate(rot)}
    adj = [[] for _ in rot]
    for u, vs in g.items():
        for v in vs:
            adj[id_[u]].append(id_[v])
    return adj, id_, rot


def rankear_adj(adj):
    alvo = lambda e: e[0] if isinstance(e, tuple) else e
    usados = {u for u in range(len(adj)) if adj[u]} | {alvo(e) for es in adj for e in es}
    rot = sorted(usados)
    id_ = {x: i for i, x in enumerate(rot)}
    novo = [[] for _ in rot]
    for u in rot:
        for e in adj[u]:
            novo[id_[u]].append((id_[e[0]],) + tuple(e[1:]) if isinstance(e, tuple) else id_[e])
    return novo, id_, rot


D4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
D8 = D4 + ((1, 1), (1, -1), (-1, 1), (-1, -1))
def vizinhos(r, c, n, m, D=D4):
    for dr, dc in D:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            yield nr, nc


def rank(a):
    vals = sorted(set(a))
    rk = {v: i for i, v in enumerate(vals)}
    return vals, rk, [rk[x] for x in a]


def argsort(a):
    idx = sorted(range(len(a)), key=lambda i: a[i])
    pos = [0] * len(a)
    for k, i in enumerate(idx): pos[i] = k
    return idx, pos


MOD = 10**9 + 7
N = 10**6
fat = [1] * (N + 1)
for i in range(1, N + 1): fat[i] = fat[i - 1] * i % MOD
inv_fat = [1] * (N + 1)
inv_fat[N] = pow(fat[N], MOD - 2, MOD)
for i in range(N, 0, -1): inv_fat[i - 1] = inv_fat[i] * i % MOD

def C(n, k):
    if k < 0 or k > n: return 0
    return fat[n] * inv_fat[k] % MOD * inv_fat[n - k] % MOD


def fatora(x):
    f = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            f[d] = f.get(d, 0) + 1; x //= d
        d += 1
    if x > 1: f[x] = f.get(x, 0) + 1
    return f


def divisores(x):
    ds = []
    d = 1
    while d * d <= x:
        if x % d == 0:
            ds.append(d)
            if d != x // d: ds.append(x // d)
        d += 1
    return sorted(ds)


def eh_primo(x):
    if x < 2: return False
    d = 2
    while d * d <= x:
        if x % d == 0: return False
        d += 1
    return True


def menor_fator(n):
    mf = list(range(n + 1))
    for i in range(2, int(n ** .5) + 1):
        if mf[i] == i:
            for j in range(i * i, n + 1, i):
                if mf[j] == j: mf[j] = i
    return mf

def fatora_mf(x, mf):
    f = {}
    while x > 1:
        p = mf[x]; f[p] = f.get(p, 0) + 1; x //= p
    return f


def itens(mask):
    while mask:
        b = mask & -mask
        yield b.bit_length() - 1
        mask ^= b


def escolhas(lista):
    n = len(lista)
    for mask in range(1 << n):
        yield mask, [lista[i] for i in range(n) if mask >> i & 1]


def submascaras(mask):
    sub = mask
    while sub:
        yield sub
        sub = (sub - 1) & mask


def maior_viavel(lo, hi, ok):
    r = lo - 1
    while lo <= hi:
        m = (lo + hi) // 2
        if ok(m): r = m; lo = m + 1
        else: hi = m - 1
    return r

def menor_viavel(lo, hi, ok):
    r = hi + 1
    while lo <= hi:
        m = (lo + hi) // 2
        if ok(m): r = m; hi = m - 1
        else: lo = m + 1
    return r


def menor_dos_lados(a):
    n = len(a); l = [-1] * n; r = [n] * n; s = []
    for i in range(n):
        while s and a[s[-1]] >= a[i]: s.pop()
        if s: l[i] = s[-1]
        s.append(i)
    s = []
    for i in range(n - 1, -1, -1):
        while s and a[s[-1]] >= a[i]: s.pop()
        if s: r[i] = s[-1]
        s.append(i)
    return l, r


class Mediana:
    def __init__(s):
        s.lo = []; s.hi = []
    def add(s, x):
        if not s.lo or x <= -s.lo[0]: heapq.heappush(s.lo, -x)
        else: heapq.heappush(s.hi, x)
        if len(s.lo) > len(s.hi) + 1: heapq.heappush(s.hi, -heapq.heappop(s.lo))
        elif len(s.hi) > len(s.lo): heapq.heappush(s.lo, -heapq.heappop(s.hi))
    def get(s):
        return -s.lo[0] if len(s.lo) > len(s.hi) else (-s.lo[0] + s.hi[0]) / 2


def bfs(adj, s):
    d = [-1] * len(adj); d[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1; q.append(v)
    return d


def bfs_pai(adj, s):
    d = [-1] * len(adj); pai = [-1] * len(adj); ordem = []; d[s] = 0; q = deque([s])
    while q:
        u = q.popleft(); ordem.append(u)
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1; pai[v] = u; q.append(v)
    return d, pai, ordem

def caminho(pai, t):
    c = []
    while t != -1:
        c.append(t); t = pai[t]
    return c[::-1]


def bfs_grid(g, sr, sc):
    n, m = len(g), len(g[0])
    d = [[-1] * m for _ in range(n)]; d[sr][sc] = 0; q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and g[nr][nc] != '#' and d[nr][nc] == -1:
                d[nr][nc] = d[r][c] + 1; q.append((nr, nc))
    return d


def dfs_ordem(adj, s):
    pai = [-1] * len(adj); vis = [False] * len(adj); ordem = []; st = [s]; vis[s] = True
    while st:
        u = st.pop(); ordem.append(u)
        for v in adj[u]:
            if not vis[v]:
                vis[v] = True; pai[v] = u; st.append(v)
    return ordem, pai


def tamanhos(ordem, pai):
    sz = [1] * len(pai)
    for u in reversed(ordem):
        if pai[u] != -1: sz[pai[u]] += sz[u]
    return sz

def profundidades(ordem, pai):
    dep = [0] * len(pai)
    for u in ordem:
        if pai[u] != -1: dep[u] = dep[pai[u]] + 1
    return dep


def lifting(pai):
    n = len(pai)
    up = [[v if p == -1 else p for v, p in enumerate(pai)]]
    for _ in range(max(1, (n - 1).bit_length()) - 1):
        ant = up[-1]
        up.append([ant[ant[v]] for v in range(n)])
    return up

def subir(up, v, k):
    j = 0
    while k:
        if k & 1: v = up[j][v]
        k >>= 1; j += 1
    return v

def lca(up, dep, a, b):
    if dep[a] < dep[b]: a, b = b, a
    a = subir(up, a, dep[a] - dep[b])
    if a == b: return a
    for j in range(len(up) - 1, -1, -1):
        if up[j][a] != up[j][b]:
            a, b = up[j][a], up[j][b]
    return up[0][a]


class DSU:
    def __init__(s, n):
        s.p = list(range(n)); s.sz = [1] * n
    def find(s, x):
        r = x
        while s.p[r] != r: r = s.p[r]
        while s.p[x] != r: s.p[x], x = r, s.p[x]
        return r
    def union(s, a, b):
        a, b = s.find(a), s.find(b)
        if a == b: return False
        if s.sz[a] < s.sz[b]: a, b = b, a
        s.p[b] = a; s.sz[a] += s.sz[b]
        return True


def dijkstra(adj, s):
    d = [INF] * len(adj); d[s] = 0; h = [(0, s)]
    while h:
        du, u = heapq.heappop(h)
        if du > d[u]: continue
        for v, w in adj[u]:
            if du + w < d[v]:
                d[v] = du + w; heapq.heappush(h, (d[v], v))
    return d


def prim(adj, s):
    vis = [False] * len(adj); vis[s] = True; total = 0; ligados = 1
    h = [(w, v) for v, w in adj[s]]; heapq.heapify(h)
    while h:
        w, v = heapq.heappop(h)
        if vis[v]: continue
        vis[v] = True; total += w; ligados += 1
        for x, wx in adj[v]:
            if not vis[x]: heapq.heappush(h, (wx, x))
    return total, ligados


def bellman(n, arestas, s):
    d = [INF] * n; d[s] = 0
    for _ in range(n - 1):
        for u, v, w in arestas:
            if d[u] + w < d[v]: d[v] = d[u] + w
    for u, v, w in arestas:
        if d[u] + w < d[v]: return None
    return d


def floyd(d):
    n = len(d)
    for k in range(n):
        dk = d[k]
        for i in range(n):
            dik = d[i][k]
            if dik == INF: continue
            di = d[i]
            for j in range(n):
                if dik + dk[j] < di[j]: di[j] = dik + dk[j]
    return d


def kahn(adj, ini=0):
    n = len(adj); entra = [0] * n
    for u in range(ini, n):
        for v in adj[u]: entra[v] += 1
    q = deque(i for i in range(ini, n) if entra[i] == 0); ordem = []
    while q:
        u = q.popleft(); ordem.append(u)
        for v in adj[u]:
            entra[v] -= 1
            if entra[v] == 0: q.append(v)
    return ordem


def conta_caminhos(adj, fim, MOD):
    val = [0] * len(adj)
    val[fim] = 1
    for u in reversed(kahn(adj, 1)):
        for v in adj[u]:
            val[u] = (val[u] + val[v]) % MOD
    return val


def lis(a, estrita=True):
    acha = bisect.bisect_left if estrita else bisect.bisect_right
    t = []
    for x in a:
        k = acha(t, x)
        if k == len(t): t.append(x)
        else: t[k] = x
    return len(t)


def dp_bitmask(n, pode, MOD):
    dp = [0] * (1 << n)
    dp[0] = 1
    for mask in range(1 << n):
        if dp[mask] == 0: continue
        i = bin(mask).count('1')
        if i == n: continue
        for j in range(n):
            if not mask >> j & 1 and pode[i][j]:
                novo = mask | (1 << j)
                dp[novo] = (dp[novo] + dp[mask]) % MOD
    return dp


class Fenwick:
    def __init__(s, n, a=None):
        s.n = n; s.t = [0] * (n + 1)
        if a:
            for i in range(1, n + 1):
                s.t[i] += a[i - 1]
                j = i + (i & -i)
                if j <= n: s.t[j] += s.t[i]
    def update(s, i, v):
        while i <= s.n:
            s.t[i] += v; i += i & -i
    def prefixo(s, i):
        r = 0
        while i > 0:
            r += s.t[i]; i -= i & -i
        return r
    def query(s, l, r):
        return s.prefixo(r) - s.prefixo(l - 1)


class SegTree:
    def __init__(s, a, op, neutro):
        s.n = len(a); s.op = op; s.e = neutro
        s.P = 1 << (s.n - 1).bit_length()
        s.t = [neutro] * (2 * s.P)
        s.t[s.P:s.P + s.n] = a
        for i in range(s.P - 1, 0, -1):
            s.t[i] = op(s.t[2 * i], s.t[2 * i + 1])
    def set(s, i, v):
        i += s.P; s.t[i] = v
        while i > 1:
            i //= 2
            s.t[i] = s.op(s.t[2 * i], s.t[2 * i + 1])
    def get(s, i):
        return s.t[i + s.P]
    def query(s, l, r):
        res = s.e
        l += s.P; r += s.P
        while l <= r:
            if l & 1: res = s.op(res, s.t[l]); l += 1
            if not r & 1: res = s.op(res, s.t[r]); r -= 1
            l //= 2; r //= 2
        return res


def sparse_build(a, op=min):
    n = len(a); sp = [a[:]]
    k = 1
    while 2 * k <= n:
        prev = sp[-1]
        sp.append([op(prev[i], prev[i + k]) for i in range(n - 2 * k + 1)])
        k *= 2
    return sp

def sparse_query(sp, l, r, op=min):
    j = (r - l + 1).bit_length() - 1
    return op(sp[j][l], sp[j][r - (1 << j) + 1])


def pi_kmp(s):
    pi = [0] * len(s)
    for i in range(1, len(s)):
        k = pi[i - 1]
        while k and s[i] != s[k]: k = pi[k - 1]
        if s[i] == s[k]: k += 1
        pi[i] = k
    return pi

def ocorrencias(t, p):
    pi = pi_kmp(p + '\x00' + t); m = len(p)
    return [i - 2 * m for i in range(len(pi)) if pi[i] == m]


def crivo(n):
    p = bytearray([1]) * (n + 1); p[0] = 0
    if n >= 1: p[1] = 0
    for i in range(2, int(n ** .5) + 1):
        if p[i]: p[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return p


def mult(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            r[i + j] += ca * cb
    return r

def avalia(p, x):
    r = 0
    for c in reversed(p):
        r = r * x + c
    return r
