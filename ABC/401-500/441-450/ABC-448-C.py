# ABC-448 C - Except and Min
# https://atcoder.jp/contests/abc448/tasks/abc448_c
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def getInt():
    return int(input())


def main():
    N, Q = getIntMap()
    A = getIntList()

    # Aの要素を昇順にソートして、最小値から6番目までをDに保存する
    # クエリでピックアップされる数字が最大5つであるため6番目までを保存する
    D = sorted(A)[0:6]

    # クエリを順番に見ていく
    for _ in range(Q):
        K = getInt()
        B = getIntList()
        # ピックアップされた数字をCに保存する（インデックスを補正）
        C = [A[b - 1] for b in B]

        # Dのコピーを作成して、Cに含まれる数字を削除する
        # 同一要素が複数ある場合を考慮して実際に削除していく
        d = D.copy()
        for c in C:
            if c in d:
                # cがDに含まれている場合は、Dからcを削除する
                d.remove(c)
        # Dの最小値を出力する
        print(min(d))


if __name__ == "__main__":
    main()
