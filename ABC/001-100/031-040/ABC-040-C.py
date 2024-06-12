# ABC-040 C - 柱柱柱柱柱
# https://atcoder.jp/contests/abc040/tasks/abc040_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()
    c1 = [0] + [abs(a[i] - a[i - 1]) for i in range(1, n)]
    c2 = [0, 0] + [abs(a[i] - a[i - 2]) for i in range(2, n)]

    dp = []

    dp.append(0)
    dp.append(c1[1])

    for i in range(2, n):
        x = dp[i - 1] + c1[i]
        y = dp[i - 2] + c2[i]

        dp.append(min(x, y))

    print(dp[-1])


if __name__ == "__main__":
    main()
