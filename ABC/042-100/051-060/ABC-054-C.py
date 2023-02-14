# ABC-054 C - One-stroke Path
# https://atcoder.jp/contests/abc054/tasks/abc054_c
#
import itertools


def getIntMap():
    return map(int, input().split())


def getIntListRow(N):
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    n, m = getIntMap()
    k = getIntListRow(m)

    p = [i + 1 for i in range(n)]

    # 先頭を除外して順列を作る
    s = p.pop(0)
    l = itertools.permutations(p, len(p))

    c = 0
    for v in l:
        # 先頭を戻して経路をチェック
        # k内に存在しなければチェック終了
        w = [s] + list(v)
        a = 0
        for i in range(len(w) - 1):
            x = [w[i], w[i + 1]]
            x.sort()
            if not x in k:
                break
            else:
                a += 1
        # 経路数がn-1だったらカウント
        if a == (n - 1):
            c += 1
    print(c)


if __name__ == "__main__":
    main()
