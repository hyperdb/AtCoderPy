# ABC-262 B - Triangle (Easier)
# https://atcoder.jp/contests/abc262/tasks/abc262_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m = getIntMap()
    uv = getIntListRow(m)
    c = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(m):
        u, v = uv[i]
        c[u][v] = True
        c[v][u] = True

    r = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                if c[i][j] and c[j][k] and c[k][i]:
                    r += 1
    print(r)


if __name__ == "__main__":
    main()
