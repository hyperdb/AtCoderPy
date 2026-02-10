# ABC-443 C - Chokutter Addiction
# https://atcoder.jp/contests/abc443/tasks/abc443_c
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, T = getIntMap()
    A = getIntList()

    open_at = 0
    viewed = 0
    for a in A:
        if open_at < a:
            viewed += a - open_at
            open_at = a + 100  # 次に開く時間
        # else:
        # まだ開いていない場合は何もしない

    # 最後に開いてから終了時間まで見ている分を加える
    if open_at < T:
        viewed += T - open_at

    print(viewed)


if __name__ == "__main__":
    main()
