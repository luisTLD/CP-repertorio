# CSES 1647 - Static Range Minimum Queries
# https://cses.fi/problemset/task/1647
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n, q = ni(), ni()
    x = [ni() for _ in range(n)]

    sp = [[float('inf')] * (n + 1) for _ in range(n.bit_length())]
    for j in range(1, n + 1): sp[0][j] = x[j - 1]
    for i in range(1, n.bit_length()):
        for j in range(1, n - ((2**i) - 1) + 1):
            sp[i][j] = min(sp[i - 1][j], sp[i - 1][j + (2**(i - 1))])

    for _ in range(q):
        l, r = ni(), ni()
        diff = r - l + 1
        i = diff.bit_length() - 1
        out.append(min(sp[i][l], sp[i][r - (2**i) + 1]))

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
