# ABC-151 B - Achieve the Goal
# https://atcoder.jp/contests/abc151/tasks/abc151_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k, m = getIntMap()
    a = getIntList()

    b = max(0, n * m - sum(a))

    print(b if b <= k else -1)


if __name__ == "__main__":
    main()
