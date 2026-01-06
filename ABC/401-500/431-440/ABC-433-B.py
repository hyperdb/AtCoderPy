# ABC-433 B - Nearest Taller
# https://atcoder.jp/contests/abc433/tasks/abc433_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = [0] + getIntList()

    for i in range(1, N + 1):
        p = -1
        for j in range(i):
            if A[j] > A[i]:
                p = max(p, j)
        print(p)


if __name__ == "__main__":
    main()
