# ABC-448 A - chmin
# https://atcoder.jp/contests/abc448/tasks/abc448_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, X = getIntMap()
    A = getIntList()

    # Aの要素を順番に見ていく
    for a in A:
        # aがXより小さい場合は、Xをaに更新して1を出力する
        if a < X:
            print(1)
            X = a
        # そうでない場合は、Xを更新せずに0を出力する
        else:
            print(0)


if __name__ == "__main__":
    main()
