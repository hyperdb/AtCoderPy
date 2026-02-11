# ABC-062 C - Chocolate Bar
# https://atcoder.jp/contests/abc062/tasks/arc074_a
#
def getIntMap():
    return map(int, input().split())


def divide3(n, m):
    # 三等分できれば0
    # そうでなければ余りを分配
    return 0 if n % 3 == 0 else m


def divide2x2(n, m):
    result = n * m
    # nを2つに分けて、片側をさらに2つに分ける
    for i in range(1, n):
        x1 = i
        x2 = n - i

        area1 = x1 * m

        # 二等分できれば残りを二等分
        if m % 2 == 0:
            area2 = x2 * (m // 2)
            area3 = area2
        # そうでなければ余りを分配
        else:
            area2 = x2 * (m // 2)
            area3 = x2 * (m // 2 + 1)

        # 最小値を更新
        max_area = max(area1, area2, area3)
        min_area = min(area1, area2, area3)

        result = min(result, max_area - min_area)

    return result


def main():
    H, W = getIntMap()

    # 一辺を3つに分けるパターン
    div3 = min(divide3(H, W), divide3(W, H))

    # 辺を2つに分けて、片側をさらに2つに分けるパターン
    div2x2 = min(divide2x2(H, W), divide2x2(W, H))

    print(min(div3, div2x2))


if __name__ == "__main__":
    main()
