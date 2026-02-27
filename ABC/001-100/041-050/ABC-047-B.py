# ABC-047 B - すぬけ君の塗り絵 2 イージー
# https://atcoder.jp/contests/abc047/tasks/abc047_b
#
def getIntMap() -> tuple[int, int, int]:
    return tuple(map(int, input().split()))


def getIntList() -> list[int]:
    return list(map(int, input().split()))


def getIntListRow(N: int) -> list[list[int]]:
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    W: int
    H: int
    N: int
    W, H, N = getIntMap()
    L: list[list[int]] = getIntListRow(N)

    M: list[list[int]] = [[1 for _ in range(W)] for _ in range(H)]

    row: list[int]
    for row in L:
        if row[2] == 1:
            for i in range(H):
                for j in range(row[0]):
                    M[i][j] = 0
        elif row[2] == 2:
            for i in range(H):
                for j in range(row[0], W):
                    M[i][j] = 0
        elif row[2] == 3:
            for i in range(row[1]):
                for j in range(W):
                    M[i][j] = 0
        else:
            for i in range(row[1], H):
                for j in range(W):
                    M[i][j] = 0

    print(sum(sum(row) for row in M))


if __name__ == "__main__":
    main()
