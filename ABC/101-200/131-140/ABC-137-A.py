# ABC-137 A - +-x
# https://atcoder.jp/contests/abc137/tasks/abc137_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(max([a + b, a - b, a * b]))


if __name__ == "__main__":
    main()
