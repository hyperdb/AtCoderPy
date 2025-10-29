# ABC-421 A - Misdelivery
# https://atcoder.jp/contests/abc421/tasks/abc421_a
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def getStringMap():
    return input().split()


def main():
    N = getInt()
    S = getStringRow(N)
    X, Y = getStringMap()

    print("Yes" if S[int(X) - 1] == Y else "No")


if __name__ == "__main__":
    main()
