# AtCoder ABC038 D - Present
# https://atcoder.jp/contests/abc038/tasks/abc038_d
import sys
import bisect

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()
    boxs = [(ni(), ni()) for _ in range(n)]
    boxs.sort(key=lambda b: (b[0], -b[1]))

    using = []
    for _, bj in boxs:
        i = bisect.bisect_left(using, bj)
        if i == len(using):
            using.append(bj)
        else:
            using[i] = bj

    out.append(len(using))
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
