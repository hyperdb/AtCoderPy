# ABC-458 B - Count Adjacent Cells
# https://atcoder.jp/contests/abc458/tasks/abc458_b
#
def getIntMap():
    return map(int, input().split())


def main():
    H, W = getIntMap()

    for h in range(H):
        buffer = []
        for w in range(W):
            # 周囲が隣接する辺の最大数
            side = 4
            # 上下左右の端にいる場合は辺の数を減らす
            if h == 0:
                side -= 1
            if h == H - 1:
                side -= 1
            if w == 0:
                side -= 1
            if w == W - 1:
                side -= 1
            # 出力用のバッファに辺の数を追加
            buffer.append(str(side))
        # 1行ずつ出力
        print(" ".join(buffer))


if __name__ == "__main__":
    main()
