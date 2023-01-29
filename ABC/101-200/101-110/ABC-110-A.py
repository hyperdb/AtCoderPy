# ABC-110 A - Maximize the Formula
# https://atcoder.jp/contests/abc110/tasks/abc110_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    n = getIntList()

    n.sort()
    n[2] = n[2] * 10

    print(sum(n))


if __name__ == "__main__":
    main()
