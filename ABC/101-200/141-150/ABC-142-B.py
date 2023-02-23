# ABC-142 B - Roller Coaster
# https://atcoder.jp/contests/abc142/tasks/abc142_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k = getIntMap()
    h = getIntList()

    print(sum([1 for i in h if i >= k]))


if __name__ == "__main__":
    main()
