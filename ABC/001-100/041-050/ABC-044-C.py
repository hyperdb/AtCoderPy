# ABC-044 C - 高橋君とカード
# https://atcoder.jp/contests/abc044/tasks/arc060_a
#
# 参考： https://atcoder.jp/contests/abc044/submissions/36687846
import itertools


def getIntMapt():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, a = getIntMapt()
    x = getIntList()

    s = sum(x)
    dp = [[0] * (s + 1) for _ in range(n)]

    for i in range(n):
        v = x[i]
        if i > 0:
            for j in range(s + 1):
                dp[i][j] = dp[i - 1][j]
        for k in range(s + 1):
            if dp[i - 1][k] > 0:
                dp[i][k + v] += 1
        dp[i][v] += 1

    c = 0
    for i in range(1, s + 1):
        if i % a == 0:
            c += dp[n - 1][i]

    print(c)


if __name__ == "__main__":
    main()
