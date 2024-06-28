# ABC-010 B - 花占い
# https://atcoder.jp/contests/abc010/tasks/abc010_2
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()
    b = [3, 0, 1, 0, 1, 2]
    # oxoxox oxoxox oxoxox
    # oxooxo oxooxo oxooxo

    r = 0
    for x in a:
        f = x % 6
        r += b[f]

    print(r)


if __name__ == "__main__":
    main()