# ABC-084 C - Special Trains
# https://atcoder.jp/contests/abc084/tasks/abc084_c
#
def getInt():
    return int(input())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    d = [[]] + getIntListRow(N - 1)

    for i in range(1, N):
        # 経過時間（次駅での出発時間判定に使う）
        t = 0
        for j in range(i, N):
            c, s, f = d[j]
            # 始発に間に合わない場合
            if t > s:
                diff = t - s  # 遅延時間
                s = (diff + f - 1) // f * f + s

            # 直前までの経過時間はsに含まれている
            t = s + c
        print(t)

    # N駅からは移動しない
    print(0)


if __name__ == "__main__":
    main()
