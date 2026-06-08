# ABC-460 B - Two Rings
# https://atcoder.jp/contests/abc460/tasks/abc460_b
#
def getInt():
    return int(input())


def getIntMap():
    return map(int, input().split())


def main():
    T = getInt()

    for _ in range(T):
        X1, Y1, R1, X2, Y2, R2 = getIntMap()

        # 中心の距離（２乗）
        distance = (X1 - X2) ** 2 + (Y1 - Y2) ** 2
        # 半径の和と差（２乗）
        radius_sum = (R1 + R2) ** 2
        radius_diff = (R1 - R2) ** 2

        print("Yes" if radius_diff <= distance <= radius_sum else "No")


if __name__ == "__main__":
    main()
