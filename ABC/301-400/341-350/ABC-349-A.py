# ABC-349 A - Zero Sum Game
# https://atcoder.jp/contests/abc349/tasks/abc349_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    print(0 - sum(a))


if __name__ == "__main__":
    main()
