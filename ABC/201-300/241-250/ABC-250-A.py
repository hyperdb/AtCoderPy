# ABC-250 A - Adjacent Squares
# https://atcoder.jp/contests/abc250/tasks/abc250_a
#
def getIntMap():
    return map(int, input().split())


def main():
    h, w = getIntMap()
    r, c = getIntMap()

    s = 0
    s += 1 if 1 < r <= h else 0
    s += 1 if 1 <= r < h else 0
    s += 1 if 1 < c <= w else 0
    s += 1 if 1 <= c < w else 0

    print(s)


if __name__ == "__main__":
    main()
