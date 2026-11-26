# AtCoder ABC464 C - Plumage Palette
# https://atcoder.jp/contests/abc464/tasks/abc464_c
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n, m = ni(), ni()
    adb = [[ni(), ni(), ni()] for _ in range(n)]

    adb.sort(key=lambda x: x[1])

    d = {}
    for adbi in adb:
        d[adbi[0]] = d.get(adbi[0], 0) + 1

    ans = len(d)

    j = 0
    for i in range(1, m + 1):
        while j < n and adb[j][1] <= i:
            d[adb[j][0]] -= 1
            if d[adb[j][0]] == 0:
                ans -= 1
            if adb[j][2] not in d or d[adb[j][2]] == 0:
                d[adb[j][2]] = 1
                ans += 1
            else:
                d[adb[j][2]] += 1
            j += 1

        out.append(ans)

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
