# ABC-272 A - Integer Sum
# https://atcoder.jp/contests/abc272/tasks/abc272_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    print(sum(a))


if __name__ == "__main__":
    main()
