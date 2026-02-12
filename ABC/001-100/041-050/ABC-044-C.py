# ABC-044 C - 高橋君とカード
# https://atcoder.jp/contests/abc044/tasks/arc060_a
#
def getIntMap() -> tuple[int, ...]:
    return tuple(map(int, input().split()))


def getIntList() -> list[int]:
    return list(map(int, input().split()))


def main():
    N: int
    A: int
    N, A = getIntMap()
    x: list[int] = getIntList()

    dp: list[list[list[int]]] = [[[0 for _ in range(N + 1)] for _ in range(N * 50 + 1)] for _ in range(N + 1)]

    dp[0][0][0] = 1

    for i in range(N):
        for j in range(sum(x)):
            for k in range(N):
                if dp[i][j][k] == 0:
                    continue
                else:
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j + x[i]][k + 1] += dp[i][j][k]

    r: int = 0
    for k in range(1, N + 1):
        r += dp[N][A * k][k]

    print(r)


if __name__ == "__main__":
    main()
