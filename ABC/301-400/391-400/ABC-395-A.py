# ABC-395 A - Strictly Increasing?
# https://atcoder.jp/contests/abc395/tasks/abc395_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()

    B = [A[i] - A[i - 1] for i in range(1, N)]

    print("Yes" if min(B) > 0 else "No")


if __name__ == "__main__":
    main()
