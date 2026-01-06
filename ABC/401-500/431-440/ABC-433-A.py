# ABC-433 A - Happy Birthday! 4
# https://atcoder.jp/contests/abc433/tasks/abc433_a
#
def getIntMap():
    return map(int, input().split())


def main():
    X, Y, Z = getIntMap()

    result = False
    if X > Y:
        for n in range(10**6):
            z = (X + n) / (Y + n)
            # 倍率を計算してZと一致したら終了
            if z == Z:
                result = True
                break
            # 結果がZを下回ったら終了
            elif z < Z:
                break
    print("Yes" if result else "No")


if __name__ == "__main__":
    main()
