# AtCoder ABC392 D - Doubles
# https://atcoder.jp/contests/abc392/tasks/abc392_d
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()
    k = []

    for i in range(n):
        tam = ni()
        ki = [ni() for _ in range(tam)]
        d = {}
        for ai in ki:
            d[ai] = d.get(ai, 0) + 1
        k.append((len(ki), d))

    p = 0
    for i in range(len(k)):
        di = k[i][1]
        for j in range(i + 1, len(k)):
            dj = k[j][1]
            repetition = 0
            for v in di.keys():
                repetition += di.get(v, 0) * dj.get(v, 0)
            p = max(p, repetition / (k[i][0] * k[j][0]))

    out.append(p)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
