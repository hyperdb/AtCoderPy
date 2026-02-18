# ABC-444 C - AtCoder Riko
# https://atcoder.jp/contests/abc444/tasks/abc444_c
#
from collections import deque


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    A = getIntList()

    # Lの候補は最大値と最大値+最小値の2つ
    S = [max(A), max(A) + min(A)]
    ans = []

    # Sを1つずつ試す
    for s in S:
        # AからLを除いたものをaとする
        a = [a for a in A if a != s]
        # aを昇順にソートしてdequeにする
        a.sort()
        b = deque(a)
        # bの両端を見て和がLでないものがあれば終了
        while b:
            # bの長さが1なら終了
            if len(b) == 1:
                break
            # bの両端の和がLでないなら終了
            elif b[0] + b[-1] != s:
                break
            # bの両端の和がLなら両端を削除して続行
            else:
                b.popleft()
                b.pop()

        # bが空ならsは条件を満たす
        if not b:
            ans.append(s)

    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
