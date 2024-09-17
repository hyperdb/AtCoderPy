# ABC-368 B - Decrease 2 max elements
# https://atcoder.jp/contests/abc368/tasks/abc368_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def checker(x):
    return len([i for i in x if i > 0])


def main():
    N = getInt()
    A = getIntList()

    c = 0
    while checker(A) > 1:
        A.sort()
        for i in range(N - 2, N):
            A[i] -= 1
        c += 1
    print(c)


if __name__ == "__main__":
    main()
