# ABC-390 B - Geometric Sequence
# https://atcoder.jp/contests/abc390/tasks/abc390_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()

    r = True
    if N > 2:
        for i in range(N - 2):
            # 等比中項
            if A[i] * A[i + 2] != A[i + 1] ** 2:
                r = False
                break

    print("Yes" if r else "No")


if __name__ == "__main__":
    main()
