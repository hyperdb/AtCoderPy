# ABC-365 B - Second Best
# https://atcoder.jp/contests/abc365/tasks/abc365_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()
    B = sorted(A)

    print(A.index(B[N - 2]) + 1)


if __name__ == "__main__":
    main()
