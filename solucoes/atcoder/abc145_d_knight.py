# AtCoder ABC145 D - Knight
# https://atcoder.jp/contests/abc145/tasks/abc145_d
import sys

def main():
    MOD = 10**9 + 7
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    x, y = ni(), ni()
    a = (2*y - x) / 3
    b = (2*x - y) / 3
    if a < 0 or b < 0 or a % 1 != 0 or b % 1 != 0:
        out.append(0)
    else:
        a = int(a)
        b = int(b)
        n = a + b
        nf = 1
        af = 1
        bf = 1
        for i in range(2, n + 1):
            nf = (nf * i) % MOD
        for i in range(2, a + 1):
            af = (af * i) % MOD
        for i in range(2, b + 1):
            bf = (bf * i) % MOD
        out.append(nf * pow(af, MOD - 2, MOD) * pow(bf, MOD - 2, MOD) % MOD)

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
