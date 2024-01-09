# ABC-330 A - Counting Passes
# https://atcoder.jp/contests/abc330/tasks/abc330_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, l = getIntMap()
    a = getIntList()

    print(len([x for x in a if x >= l]))


if __name__ == "__main__":
    main()
