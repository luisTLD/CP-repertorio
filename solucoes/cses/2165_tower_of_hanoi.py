# CSES 2165 - Tower of Hanoi
# https://cses.fi/problemset/task/2165
import sys

def main():
    out = []

    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))

    n = ni()
    movimentos = []

    def hanoi(n, x, y, z):
        if n == 1:
            movimentos.append((x, z))
            return

        hanoi(n - 1, x, z, y)
        movimentos.append((x, z))
        hanoi(n - 1, y, x, z)

    hanoi(n, 1, 2, 3)

    out.append(len(movimentos))

    for a, b in movimentos:
        out.append(f"{a} {b}")

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
