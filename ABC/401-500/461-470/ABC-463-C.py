# ABC-463 C - Tallest at the Moment
# https://atcoder.jp/contests/abc463/tasks/abc463_c
#
from collections import deque


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = getInt()
    HL = getIntListRow(N)
    Q = getInt()
    T = getIntList()
    ST = sorted(T)

    # 時間時点での高さを記録する辞書
    R = dict()
    for t in T:
        R[t] = 0
    # 背の高さの降順でソートして、時間の昇順で処理する
    HL.sort(key=lambda x: x[0], reverse=True)
    dq = deque(HL)

    # 一番高い人から順に取り出す
    hight, limit = dq.popleft()
    for time in ST:
        # 時間が制限時間を超えていなければ、辞書に記録して次の時間へ
        if time < limit:
            R[time] = hight
            continue
        # 時間が制限時間を超えていれば、次の人を取り出す
        while dq:
            hight, limit = dq.popleft()
            if time < limit:
                R[time] = hight
                break

    # 元の順序で辞書を参照して出力する
    for t in T:
        print(R[t])


if __name__ == "__main__":
    main()
