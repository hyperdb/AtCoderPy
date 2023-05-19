# ABC-094 B - Toll Gates
# https://atcoder.jp/contests/abc094/tasks/abc094_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, m, x = getIntMap()
    a = getIntList()

    l = len([i for i in a if i < x])
    r = len([i for i in a if i > x])

    print(l if l <= r else r)


if __name__ == "__main__":
    main()
