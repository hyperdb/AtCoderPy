# ABC-108 B - Ruined Square
# https://atcoder.jp/contests/abc108/tasks/abc108_b
#
def getIntMap():
    return map(int, input().split())


def main():
    x1, y1, x2, y2 = getIntMap()

    x = x2 - x1
    y = y2 - y1

    x3 = x2 - y
    y3 = y2 + x

    x4 = x1 - y
    y4 = y1 + x

    print("%d %d %d %d" % (x3, y3, x4, y4))


if __name__ == "__main__":
    main()
