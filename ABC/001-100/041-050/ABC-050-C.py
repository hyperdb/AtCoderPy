# ABC-050 C - Lining Up
# https://atcoder.jp/contests/abc050/tasks/arc066_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()
    A.sort()

    B = 10**9 + 7

    r = True
    if N % 2 == 1:
        if A[0] != 0:
            r = False
        for i in range(1, N, 2):
            if A[i] != A[i + 1]:
                r = False
                break
            if A[i] % 2 != 0:
                r = False
                break
    else:
        for i in range(0, N, 2):
            if A[i] != A[i + 1]:
                r = False
                break
            if A[i] % 2 == 0:
                r = False
                break

    print((2 ** (N // 2)) % B if r else 0)


if __name__ == "__main__":
    main()
