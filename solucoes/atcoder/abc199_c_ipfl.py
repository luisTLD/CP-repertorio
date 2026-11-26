# AtCoder ABC199 C - IPFL
# https://atcoder.jp/contests/abc199/tasks/abc199_c
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    ns = lambda: next(it).decode()
    out = []

    n = ni()
    s = list(ns())
    q = ni()

    original = True
    for _ in range(q):
        t, a, b = ni(), ni(), ni()

        if t == 2:
            original = not original
            continue

        if original is True:
            s[a-1], s[b-1] = s[b-1], s[a-1]

        if original is False:
            if a <= n and b > n:
                s[(a-1)+n], s[(b-1)-n] = s[(b-1)-n], s[(a-1)+n]
            elif a > n:
                s[(a-1)-n], s[(b-1)-n] = s[(b-1)-n], s[(a-1)-n]
            else:
                s[(a-1)+n], s[(b-1)+n] = s[(b-1)+n], s[(a-1)+n]

    if original is False:
        s[0:n], s[n:n*2] = s[n:n*2], s[0:n]

    out.append("".join(s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
