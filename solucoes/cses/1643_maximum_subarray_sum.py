# CSES 1643 - Maximum Subarray Sum
# https://cses.fi/problemset/task/1643
import sys

def main():
    out = []

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n = ni()
    a = [ni() for _ in range(n)]
    ans, actual = -float('inf'), 0
    for ai in a:
        actual += ai
        ans = max(ans, actual)
        actual = max(actual, 0)

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")
main()
