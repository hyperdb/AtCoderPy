# ABC-455 B - Spiral Galaxy
# https://atcoder.jp/contests/abc455/tasks/abc455_b
#
def getIntMap():
    return map(int, input().split())


def getStringRow(N):
    return [list(input()) for _ in range(N)]


def main():
    H, W = getIntMap()
    S = getStringRow(H)

    # 全探索

    ans = 0
    # 開始点を決める
    for h in range(H):
        for w in range(W):
            # print(f"H={h}, W={w}")
            # 幅と高さを決める
            for dh in range(h, H):
                for dw in range(w, W):
                    # 長方形を切り出す（文字列として）
                    s = ""
                    for y in range(h, dh + 1):
                        for x in range(w, dw + 1):
                            s += S[y][x]
                    # 点対称かを判定（反転させて比較）
                    t = "".join(reversed(s))
                    if s == t:
                        # print(f"  dh={dh}, dw={dw}", s, t)
                        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
