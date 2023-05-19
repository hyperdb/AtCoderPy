# ABC-196 A - Difference Max
# https://atcoder.jp/contests/abc196/tasks/abc196_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()
    c, d = getIntMap()

    print(b - c)


if __name__ == "__main__":
    main()
