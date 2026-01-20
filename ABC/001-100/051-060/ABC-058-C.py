# ABC-058 C - 怪文書
# https://atcoder.jp/contests/abc058/tasks/arc071_a
#
def getInt():
    return int(input())


def getStringRow(N):
    return [input() for _ in range(N)]


def main():
    N = getInt()
    S = getStringRow(N)
    buf = dict()

    # 文字a～zまで使用数をカウント
    # 最小値を保存
    for c in range(26):
        ch = chr(ord("a") + c)
        buf.setdefault(ch, 50)
        for s in S:
            s.count(ch)
            buf[ch] = min(buf[ch], s.count(ch))

    # 個数が1以上のものを出力
    print("".join([k * v for k, v in sorted(buf.items()) if v > 0]))


if __name__ == "__main__":
    main()
