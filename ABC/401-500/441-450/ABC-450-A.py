# ABC-450 A - 3,2,1,GO
# https://atcoder.jp/contests/abc450/tasks/abc450_a
#
def getInt():
    return int(input())


def main():
    N = getInt()
    a = []

    # 1からNまでの整数を逆順でリストに追加
    for i in range(N, 0, -1):
        a.append(i)

    # リストの要素をカンマ区切りで出力
    print(",".join(map(str, a)))


if __name__ == "__main__":
    main()
