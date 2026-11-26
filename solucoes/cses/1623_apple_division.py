# CSES 1623 - Apple Division
# https://cses.fi/problemset/task/1623
import sys

def main():
    out = []

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n = ni()
    a = [ni() for _ in range(n)]

    max_sum = sum(a)
    ans = max_sum
    for i in range(2**n):
        j = i
        actual_sum = 0
        while j > 0:
            bit = j & -j
            actual_sum += a[bit.bit_length() - 1]
            j ^= bit
        ans = min(ans, abs((max_sum - actual_sum) - actual_sum))

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
