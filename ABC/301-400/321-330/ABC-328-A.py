# ABC-328 A - Not Too Hard
# https://atcoder.jp/contests/abc328/tasks/abc328_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, x = getIntMap()
    s = getIntList()

    print(sum([i for i in s if i <= x]))


if __name__ == "__main__":
    main()
