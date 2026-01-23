# ABC-065 C - Reconciled?
# https://atcoder.jp/contests/abc065/tasks/arc076_a
#
import math


def getIntMap():
    return map(int, input().split())


def main():
    N, M = getIntMap()

    if abs(N - M) > 1:
        print(0)
    else:
        n = math.perm(N, N)
        m = math.perm(M, M)

        # N == M の場合、nmnm と mnmn で2倍
        print((n * m * 2 if N == M else n * m) % 1000000007)


if __name__ == "__main__":
    main()
