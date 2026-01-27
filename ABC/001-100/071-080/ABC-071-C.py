# ABC-071 C - Make a Rectangle
# https://atcoder.jp/contests/abc071/tasks/arc081_a
#
import collections


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    a = getIntList()

    c = dict(collections.Counter(a))
    b = []
    # 2本以上ある辺の長さを抽出
    for k, v in c.items():
        # 4本以上ある場合は正方形を作れるので2回追加
        if v >= 4:
            b.append(k)
            b.append(k)
        elif v >= 2:
            b.append(k)
    b.sort(reverse=True)

    print(b[0] * b[1] if len(b) >= 2 else 0)


if __name__ == "__main__":
    main()
