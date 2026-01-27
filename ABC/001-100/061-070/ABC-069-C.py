# ABC-069 C - 4-adjacent
# https://atcoder.jp/contests/abc069/tasks/arc080_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    a = getIntList()

    # 個数を数える
    a4 = len([x for x in a if x % 4 == 0])  # 4の倍数
    a2 = len([x for x in a if x % 2 == 0 and x % 4 != 0])  # 2の倍数だが4の倍数ではない
    a1 = len([x for x in a if x % 2 != 0])  # 奇数

    result = False
    # 判定
    if a1 == 0:
        # 奇数がない場合は必ず4の倍数 2a * 2b = 4ab
        result = True
    else:
        # 4の倍数が奇数の数以上 141414 / 14144444
        if a4 >= a1:
            result = True
        # 4の倍数が奇数の数未満
        elif a4 < a1:
            # 2の倍数が無く、4の倍数が奇数の数-1以上 14141
            if a2 == 0 and a4 + 1 >= a1:
                result = True

    print("Yes" if result else "No")


if __name__ == "__main__":
    main()
