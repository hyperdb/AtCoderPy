# ABC-277 A - ^{-1}
# https://atcoder.jp/contests/abc277/tasks/abc277_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, x = getIntMap()
    p = [0] + getIntList()

    print(p.index(x))


if __name__ == "__main__":
    main()
