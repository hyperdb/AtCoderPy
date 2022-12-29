# ABC-066 A - ringring
# https://atcoder.jp/contests/abc066/tasks/abc066_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    n = getIntList()

    n.sort()

    print(n[0] + n[1])


if __name__ == "__main__":
    main()
