# ABC-183 B - Billiards
# https://atcoder.jp/contests/abc183/tasks/abc183_b
#
def getIntMap():
    return map(int, input().split())


def main():
    sx, sy, gx, gy = getIntMap()

    rx = gx - sx
    ry = gy / sy

    df = (rx / (ry + 1)) * ry

    print(gx - df)


if __name__ == "__main__":
    main()
