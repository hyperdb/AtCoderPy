# ABC-074 C - Sugar Water
# https://atcoder.jp/contests/abc074/tasks/arc083_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B, C, D, E, F = getIntMap()

    max_rate = -1.0
    condition = (0, 0)
    # 水の最大はFなので、AとBの組み合わせで水の量を決定
    for x in range(0, F // (100 * A) + 1):
        for y in range(0, (F - 100 * A * x) // (100 * B) + 1):
            water = 100 * A * x + 100 * B * y
            if water == 0:
                continue
            if water > F:
                continue

            # 砂糖の最大はFから水の量を引いた量なので、CとDの組み合わせで砂糖の量を決定
            for m in range(0, (F - water) // C + 1):
                for n in range(0, (F - water - C * m) // D + 1):
                    sugar = C * m + D * n
                    if water + sugar > F:
                        continue
                    if sugar > (E * water) // 100:
                        continue

                    rate = sugar / (water + sugar)
                    if rate > max_rate:
                        max_rate = rate
                        condition = (water + sugar, sugar)

    # 1回も更新されていない（砂糖が一切入っていない）場合
    if max_rate < 0:
        # 最低限の水を入れる
        condition = (100 * A, 0)

    print(condition[0], condition[1])


if __name__ == "__main__":
    main()
