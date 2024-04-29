# ABC-348 B - Farthest Point
# https://atcoder.jp/contests/abc348/tasks/abc348_b
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n = getInt()
    xy = [[]] + getIntListRow(n)

    for i in range(1, n + 1):
        m = 0
        d = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            a = (xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2
            if a > d:
                m = j
                d = a
        print(m)


if __name__ == "__main__":
    main()
