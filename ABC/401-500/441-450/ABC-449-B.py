# ABC-449 B - Deconstruct Chocolate
# https://atcoder.jp/contests/abc449/tasks/abc449_b
#
def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    H, W, Q = getIntMap()
    querries = getIntListRow(Q)

    for t, n in querries:
        # タイプ1: Row
        if t == 1:
            # 下からn行を計算
            m = n * W
            # Hを減らす
            H -= n
        # タイプ2: Column
        elif t == 2:
            # 右からn列を計算
            m = n * H
            # Wを減らす
            W -= n

        print(m)


if __name__ == "__main__":
    main()
