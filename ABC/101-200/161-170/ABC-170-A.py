# ABC-170 A - Five Variables
# https://atcoder.jp/contests/abc170/tasks/abc170_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    x = getIntList()

    print(x.index(0) + 1)


if __name__ == "__main__":
    main()
