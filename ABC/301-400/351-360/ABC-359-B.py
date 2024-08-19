# ABC-359 B - Couples
# https://atcoder.jp/contests/abc359/tasks/abc359_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()

    c = 0
    for i in range(2 * N - 2):
        if A[i] == A[i + 2] and A[i] != A[i + 1]:
            c += 1

    print(c)


if __name__ == "__main__":
    main()
