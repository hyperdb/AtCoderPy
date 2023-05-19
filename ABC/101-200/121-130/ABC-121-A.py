# ABC-121 A - White Cells
# https://atcoder.jp/contests/abc121/tasks/abc121_a
#
def getIntMap():
    return map(int, input().split())


def main():
    h, w = getIntMap()
    x, y = getIntMap()

    print((h - x) * (w - y))


if __name__ == "__main__":
    main()
