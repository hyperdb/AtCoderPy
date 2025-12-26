# ABC-048 C - Boxes and Candies
# https://atcoder.jp/contests/abc048/tasks/arc064_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, x = getIntMap()
    A = getIntList()
    B = [A[i - 1] + A[i] - x for i in range(1, N)]

    c = 0
    for i in range(len(B)):
        if B[i] > 0:
            b = B[i]

            bh = min(A[i + 1], b)

            B[i] = 0
            if i + 1 < len(B):
                B[i + 1] -= bh
            c += b
    print(c)


if __name__ == "__main__":
    main()
