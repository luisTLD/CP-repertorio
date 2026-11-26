# AtCoder ABC366 D - Cuboid Sum Query
# https://atcoder.jp/contests/abc366/tasks/abc366_d
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    ni = lambda: int(next(it))
    out = []

    n = ni()
    a = [[[ni() for _ in range(n)] for _ in range(n)] for _ in range(n)]
    q = ni()
    lr = []

    for _ in range(q):
        lri = [ni() for _ in range(6)]
        lrj = [lri[:2], lri[2:4], lri[4:]]
        lr.append(lrj)
    dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                dp[i][j][k] = (
                    ((dp[i][j-1][k] + dp[i][j][k-1]) - dp[i][j-1][k-1])
                    + (dp[i-1][j][k] - ((dp[i-1][j-1][k] + dp[i-1][j][k-1]) - dp[i-1][j-1][k-1]))
                    + a[i-1][j-1][k-1])
    for lri in lr:
        lx, rx = lri[0]
        ly, ry = lri[1]
        lz, rz = lri[2]
        ans = (dp[rx][ry][rz]
            - ((dp[lx-1][ry][rz] + dp[rx][ly-1][rz]) - dp[lx-1][ly-1][rz])
            - (dp[rx][ry][lz-1] - ((dp[lx-1][ry][lz-1] + dp[rx][ly-1][lz-1]) - dp[lx-1][ly-1][lz-1])))
        out.append(ans)

    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
