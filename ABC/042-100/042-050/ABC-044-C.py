# ABC-044 C - 高橋君とカード
# https://atcoder.jp/contests/abc044/tasks/arc060_a
#
# 参考： https://atcoder.jp/contests/abc044/submissions/36687846
def getIntMapt():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, A = getIntMapt()
    X = getIntList()

#    data = list(map(lambda x: x - A, data))
#    dp = [[0] * (N + 1) for _ in range(N + 1)]
    sumX = sum(X)
    dp = [[[0 for _ in range(sumX + 1)] for _ in range(N + 1)]
          for _ in range(N + 1)]

    dp[0][0][0] = 1
    for i in range(N):
        for j in range(N):
            for k in range(sumX):
                if dp[i][j][k] == 0:
                    continue
                dp[i + 1][j][k] += dp[i][j][k]
                dp[i + 1][j + 1][k + X[i]] += dp[i][j][k]

    ptns = 0
    for j in range(1, N+1):
        if sumX < j * A:
            continue
        ptns += dp[N][j][j * A]

    print(ptns)


if __name__ == "__main__":
    main()
