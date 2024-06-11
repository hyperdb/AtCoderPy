# ABC-064 B - Traveling AtCoDeer Problem
# https://atcoder.jp/contests/abc064/tasks/abc064_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    a.sort()

    print(a[n - 1] - a[0])


if __name__ == "__main__":
    main()
