# ABC-095 C - Half and Half
# https://atcoder.jp/contests/abc095/tasks/arc096_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B, C, X, Y = getIntMap()

    # すべてをABで賄う場合の最大値は、XとYのどちらか大きい方を2倍したもの
    maxAB = max(X, Y) * 2

    # ABを買う枚数を0からmaxABまで試す
    result = 10**15
    for ab in range(maxAB + 1):
        # ABのコスト
        cost = ab * C
        # 必要なAとBの枚数を計算
        a = X - ab // 2
        b = Y - ab // 2

        # Aの不足分を買うコスト
        if a > 0:
            cost += a * A
        # Bの不足分を買うコスト
        if b > 0:
            cost += b * B

        # 最小値を更新
        result = min(result, cost)

    print(result)


if __name__ == "__main__":
    main()
