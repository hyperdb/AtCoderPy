# A - Contest Result
# https://atcoder.jp/contests/abc290/tasks/abc290_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, m = getIntMap()
    a = [0] + getIntList()
    b = getIntList()

    c = 0
    for i in b:
        c += a[i]
    print(c)


if __name__ == "__main__":
    main()
