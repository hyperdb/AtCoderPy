#
#
#
from collections import deque


def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, M = getIntMap()
    A = getIntList()
    B = getIntList()

    # 端から取り出すためにdequeを使用
    da = deque(sorted(A))
    db = deque(sorted(B))

    count = 0
    while da and db:
        # 小さい方から取り出す
        a = da[0]  # シャリ
        b = db[0]  # ネタ

        # シャリがネタの２倍以下なら握る
        if b <= (a * 2):
            count += 1
            # シャリとネタの両方を取り除く
            da.popleft()
            db.popleft()
        else:
            # シャリのみを取り除く
            da.popleft()

    print(count)


if __name__ == "__main__":
    main()
