# ABC-072 C - Together
# https://atcoder.jp/contests/abc072/tasks/arc082_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    a = getIntList()
    b = [0] * (10**5 + 2)

    # それぞれの要素の個数を数える
    for i in range(N):
        b[a[i]] += 1

    result = 0
    for x in range(1, 10**5 + 1):
        # 計算済みの要素から隣接する要素の個数を足す
        n = b[x - 1] + b[x] + b[x + 1]
        result = max(result, n)

    print(result)


if __name__ == "__main__":
    main()
