# AtCoder ABC412 C - Giant Domino
# https://atcoder.jp/contests/abc412/tasks/abc412_c
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    t = ni()

    for _ in range(t):
        ti = ni()
        c = [ni() for _ in range(ti)]
        ans = 1

        actual = c[0]
        end = c[ti - 1]

        domino = c[1:ti - 1]
        domino.sort()
        domino.insert(0, c[0])
        domino.append(end)

        for i in range(1, ti):
            if actual * 2 >= end:
                break
            if actual * 2 >= domino[i]:
                continue
            elif domino[i - 1] * 2 < domino[i]:
                actual = domino[i - 1]
                ans += 1
                break
            else:
                actual = domino[i - 1]
                ans += 1

        out.append(ans + 1 if actual * 2 >= end else -1)

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
