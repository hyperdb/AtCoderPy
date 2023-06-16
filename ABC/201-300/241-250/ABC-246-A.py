# ABC-246 A - Four Points
# https://atcoder.jp/contests/abc246/tasks/abc246_a
#
def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    xy = getIntListRow(3)

    x = xy[2][0] if xy[0][0] == xy[1][0] else xy[0][0] if xy[1][0] == xy[2][0] else xy[1][0]
    y = xy[2][1] if xy[0][1] == xy[1][1] else xy[0][1] if xy[1][1] == xy[2][1] else xy[1][1]

    print(x, y)


if __name__ == "__main__":
    main()