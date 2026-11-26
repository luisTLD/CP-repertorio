# CSES 1649 - Dynamic Range Minimum Queries
# https://cses.fi/problemset/task/1649
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n, q = ni(), ni()
    x = []
    for _ in range(n): x.append(ni())

    t = (1 << (n - 1).bit_length()) * 2
    st = [float('inf')] * t
    for i in range(n):
        st[t-n+i] = x[i]

    for i in range(t-1, 2, -2):
        st[i//2] = min(st[i], st[i-1])

    out = []
    for _ in range(q):
        op, y, z = ni(), ni(), ni()
        if op == 2:
            py = t-n+y-1
            pz = t-n+z-1
            ans = float('inf')
            while py <= pz:
                if py % 2 == 1:
                    ans = min(ans, st[py])
                    py += 1
                if pz % 2 == 0:
                    ans = min(ans, st[pz])
                    pz -= 1
                py //= 2
                pz //= 2
            out.append(ans)
        else:
            k = t-n+y-1
            st[k] = z
            while k > 1:
                k //= 2
                st[k] = min(st[2*k], st[2*k+1])

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
