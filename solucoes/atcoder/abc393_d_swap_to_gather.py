# AtCoder ABC393 D - Swap to Gather
# https://atcoder.jp/contests/abc393/tasks/abc393_d
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    ns = lambda: next(it).decode()
    out = []

    n = ni()
    s = ns()

    positions = []
    for i, c in enumerate(s):
        if c == '1':
            positions.append(i)

    center = len(positions) // 2
    swaps = 0

    for idx, pos in enumerate(positions):
        target = positions[center] + (idx - center)
        swaps += abs(pos - target)

    out.append(swaps)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
