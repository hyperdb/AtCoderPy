# ABC-091 C - 2D Plane 2N Points
# https://atcoder.jp/contests/abc091/tasks/arc092_a
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    R = getIntListRow(N)
    B = getIntListRow(N)

    # 青い点を昇順にソートする
    blue = sorted(B)
    # 赤い点を降順にソートする（y座標が大きい順、同じ場合はx座標が大きい順）
    red = sorted(R, key=lambda x: (x[1], x[0]), reverse=True)

    # 青い点に対して赤い点を割り当てるリスト
    match = [-1] * N

    # 青い点を順番に見ていき、赤い点の中から条件を満たすものを探す
    for i in range(N):
        bx, by = blue[i]
        for j in range(N):
            # すでに割り当てられている赤い点はスキップする
            if j in match:
                continue
            rx, ry = red[j]
            if rx < bx and ry < by:
                match[i] = j
                break

    # 割り当てられた赤い点の数を数える
    print(sum([1 for x in match if x != -1]))


if __name__ == "__main__":
    main()
