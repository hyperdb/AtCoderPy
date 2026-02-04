# ABC-086 C - Traveling
# https://atcoder.jp/contests/abc086/tasks/arc089_a
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    txy = [[0, 0, 0]] + getIntListRow(N)

    # 時系列に沿ってチェック
    for i in range(1, N + 1):
        prev_t, prev_x, prev_y = txy[i - 1]
        t, x, y = txy[i]

        # 移動可能かチェック
        dt = t - prev_t  # 経過時間
        dist = abs(x - prev_x) + abs(y - prev_y)  # 移動距離

        # 移動距離が経過時間を超えている
        #  or 時間と距離の差が奇数なら不可能
        if dist > dt or (dt - dist) % 2 != 0:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
