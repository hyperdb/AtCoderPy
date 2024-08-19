# ABC-362 B - Right Triangle
# https://atcoder.jp/contests/abc362/tasks/abc362_b
#
def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def main():
    p = getIntListRow(3)
    d = [
        dist(p[0][0], p[0][1], p[1][0], p[1][1]),
        dist(p[0][0], p[0][1], p[2][0], p[2][1]),
        dist(p[1][0], p[1][1], p[2][0], p[2][1]),
    ]

    print("Yes" if sum(d) == max(d) * 2 else "No")


if __name__ == "__main__":
    main()
