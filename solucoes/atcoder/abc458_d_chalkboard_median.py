# AtCoder ABC458 D - Chalkboard Median
# https://atcoder.jp/contests/abc458/tasks/abc458_d
import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    X = ni()
    Q = ni()

    left = []
    right = []

    def add(x):
        if not left or x <= -left[0]:
            heapq.heappush(left, -x)
        else:
            heapq.heappush(right, x)

        if len(left) < len(right):
            heapq.heappush(left, -heapq.heappop(right))

        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))

    add(X)

    for _ in range(Q):
        a, b = ni(), ni()

        add(a)
        add(b)

        out.append(-left[0])

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
