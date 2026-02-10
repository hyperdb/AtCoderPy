# ABC-442 C - Peer Review
# https://atcoder.jp/contests/abc442/tasks/abc442_c
#
import math


def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N, M = getIntMap()
    ab = getIntListRow(M)
    p = [[] for _ in range(N)]
    r = [0 for _ in range(N)]

    # 関係性リストを作成
    for a, b in ab:
        p[a - 1].append(b)
        p[b - 1].append(a)

    # 研究者ごとに計算
    for i in range(N):
        member = N - len(p[i]) - 1
        # 3人に満たない場合は0通り
        if member < 3:
            continue
        # 3人の場合は1通り
        elif member == 3:
            r[i] = 1
        # 4人以上の場合は組み合わせ計算
        else:
            r[i] = math.comb(member, 3)

    print(" ".join(map(str, r)))


if __name__ == "__main__":
    main()
