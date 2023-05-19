# ABC-128 A - Apple Pie
# https://atcoder.jp/contests/abc128/tasks/abc128_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, p = getIntMap()

    print((a * 3 + p) // 2)


if __name__ == "__main__":
    main()
