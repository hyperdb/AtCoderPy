# ABC-081 C - Not so Diverse
# https://atcoder.jp/contests/abc081/tasks/arc086_a
#
import collections


def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, K = getIntMap()
    a = getIntList()

    # 種類別にカウント
    c = collections.Counter(a)
    # 種類数がK以下なら0を出力
    if len(c) <= K:
        print(0)
        return

    # 多い順に並べ替えてK個スキップして残りを合計
    d = sorted(c.values(), reverse=True)
    print(sum(d[K:]))


if __name__ == "__main__":
    main()
