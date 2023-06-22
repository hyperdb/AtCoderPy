# ABC-250 B - Enlarged Checker Board
# https://atcoder.jp/contests/abc250/tasks/abc250_b
#
def getIntMap():
    return map(int, input().split())


def mkLine(n, w, adj):
    c = ['.', '#']
    l = ''
    for i in range(n):
        l += (c[(i + adj) % 2] * w)
    return l


def main():
    n, a, b = getIntMap()

    for h in range(n):
        c = h % 2
        for w in range(a):
            l = mkLine(n, b, c)
            print(l)


if __name__ == "__main__":
    main()
