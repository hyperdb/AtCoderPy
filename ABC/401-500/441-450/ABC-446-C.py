# ABC-446 C - Omelette Restaurant
# https://atcoder.jp/contests/abc446/tasks/abc446_c
#
from collections import deque


def getInt():
    return int(input())


def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    T = getInt()

    for _ in range(T):
        N, D = getIntMap()
        A = getIntList()
        B = getIntList()

        # 両端操作なのでdequeを使用してストックを管理
        stock = deque()

        for i in range(N):
            # 卵をストック、卵の期限を記録（i+D日目まで有効）
            for _ in range(A[i]):
                stock.append(i + D)
            # 先頭から消費
            for _ in range(B[i]):
                if stock:
                    stock.popleft()
            # 期限切れの卵を先頭から削除
            while stock and stock[0] <= i:
                stock.popleft()

        # 残った卵の数を出力
        print(len(stock))


if __name__ == "__main__":
    main()
