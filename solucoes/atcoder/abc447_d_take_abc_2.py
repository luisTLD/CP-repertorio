# AtCoder ABC447 D - Take ABC 2
# https://atcoder.jp/contests/abc447/tasks/abc447_d
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ns = lambda: next(it).decode()
    out = []

    s = ns()

    a = []
    b = []
    c = []

    for i, j in enumerate(s):
        match j:
            case 'A':
                a.append(i)
            case 'B':
                b.append(i)
            case 'C':
                c.append(i)

    bi = 0
    ci = 0
    ans = 0
    for ai in a:
        if bi >= len(b) or ci >= len(c):
            break

        while bi < len(b):
            if b[bi] < ai:
                bi += 1
                continue

            if bi >= len(b) or ci >= len(c):
                break

            while ci < len(c):
                if c[ci] < b[bi]:
                    ci += 1
                else:
                    ci += 1
                    ans += 1
                    break

            bi += 1
            break

    out.append(ans)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
