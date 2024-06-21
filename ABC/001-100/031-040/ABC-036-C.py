# ABC-036 C - 座圧 ※座標圧縮
# https://atcoder.jp/contests/abc036/tasks/abc036_c
#
def getInt():
    return int(input())


def getIntRow(N):
    return [int(input()) for _ in range(N)]


def main():
    N = getInt()
    a = getIntRow(N)

    sa = sorted(set(a))

    d = dict()
    for i in range(len(sa)):
        d[sa[i]] = i

    for x in a:
        print(d[x])


if __name__ == "__main__":
    main()
