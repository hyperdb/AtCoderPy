# ABC-450 C - Puddles
# https://atcoder.jp/contests/abc450/tasks/abc450_c
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


# 白マスの領域を探索する関数
# 上下左右の白マスを探索して、境界に接しているかどうかを確認する
# 探索済みは黒マスに変えることで、再度探索されないようにする
def serchWhite(p, H, W, S):
    # 白マスを確保するリスト
    points = [p]
    is_border = False
    # 白マスの領域を探索
    while points:
        h, w = points.pop()
        # 現在のマスが境界に接しているかどうかを確認
        if h == 0 or h == H - 1 or w == 0 or w == W - 1:
            is_border = True
        # 上下左右をチェックして白マスならリストに追加して、マスを黒マスに変える
        for dh, dw in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == ".":
                S[nh][nw] = "#"
                points.append((nh, nw))

    return S, is_border


def main():
    H, W = getIntMap()
    S = getStringRow(H)

    count = 0
    # すべてのマスを走査して、白マスがあればそこから白マスの領域を探索
    for w in range(W):
        for h in range(H):
            c = S[h][w]
            if c == "#":
                continue
            # 白マスを見つけたら、そこから白マスの領域を探索して、境界に接しているかどうかを確認
            S, is_border = serchWhite((h, w), H, W, S)
            # 境界に接していない白マスの領域が見つかった場合は、カウントを増やす
            if not is_border:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
