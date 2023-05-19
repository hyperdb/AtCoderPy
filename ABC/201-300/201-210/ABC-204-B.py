# ABC-204 B - Nuts
# https://atcoder.jp/contests/abc204/tasks/abc204_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    print(sum([i - 10 for i in a if i > 10]))


if __name__ == "__main__":
    main()
