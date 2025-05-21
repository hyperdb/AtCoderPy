# ABC-403 A - Odd Position Sum
# https://atcoder.jp/contests/abc403/tasks/abc403_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()

    r = 0
    for i in range(N):
        if i % 2 == 0:
            r += A[i]

    print(r)


if __name__ == "__main__":
    main()
