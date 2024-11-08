# ABC-376 C - Prepare Another Box
# https://atcoder.jp/contests/abc376/tasks/abc376_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()
    B = getIntList()

    A.sort()
    A.reverse()
    B.sort()
    B.reverse()

    j = 0
    buy = 0
    for i in range(N):
        toy = A[i]

        # 最後の箱がない（箱は未購入）
        if i == len(B) and buy == 0:
            buy = toy
            break

        box = B[j]
        # 箱の方が大きい
        if box >= toy:
            j += 1
            continue
        # 箱が小さい
        else:
            # すでに箱を購入済み
            if buy > 0:
                buy = -1
                break
            # 箱を購入
            buy = toy
            continue

    print(buy)


if __name__ == "__main__":
    main()
