# AtCoder ABC441 C - Sake or Water
# https://atcoder.jp/contests/abc441/tasks/abc441_c
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n, k, x = ni(), ni(), ni()
    a = [ni() for _ in range(n)]

    a.sort()
    a = a[0:k]
    a.sort(reverse=True)

    count = n - k
    for i in range(k):
        count += 1
        x -= a[i]
        if x <= 0:
            break

    out.append(count if x <= 0 else -1)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
