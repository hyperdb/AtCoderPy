# ABC-437 B - Tombola
# https://atcoder.jp/contests/abc437/tasks/abc437_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    H, W, N = getIntMap()
    A = getIntListRow(H)
    B = getIntRow(N)

    C = [0] * H

    for h in range(H):
        for n in range(N):
            if B[n] in A[h]:
                C[h] += 1
    print(max(C))


if __name__ == "__main__":
    main()
