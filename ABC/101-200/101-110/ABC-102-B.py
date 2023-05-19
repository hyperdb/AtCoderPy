# ABC-102 B - Maximum Difference
# https://atcoder.jp/contests/abc102/tasks/abc102_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    print(max(a) - min(a))


if __name__ == "__main__":
    main()
