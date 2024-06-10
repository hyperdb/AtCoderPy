# ABC-356 B - Nutrients
# https://atcoder.jp/contests/abc356/tasks/abc356_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M = getIntMap()
    A = getIntList()
    X = getIntListRow(N)

    for i in range(N):
        for j in range(M):
            A[j] -= X[i][j]

    r = True
    for i in A:
        if i > 0:
            r = False
            break

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
