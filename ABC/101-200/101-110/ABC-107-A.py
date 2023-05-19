# ABC-107 A - Train
# https://atcoder.jp/contests/abc107/tasks/abc107_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, i = getIntMap()

    print(n - i + 1)


if __name__ == "__main__":
    main()
