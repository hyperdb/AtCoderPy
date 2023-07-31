# ABC-275 B - ABC-DEF
# https://atcoder.jp/contests/abc275/tasks/abc275_b
#
def getIntMap():
    return map(int, input().split())


def m3(x, y, z, a):
    return (x % a) * (y % a) * (z % a)


def main():
    a, b, c, d, e, f = getIntMap()
    div = 998244353

    print((m3(a, b, c, div) - m3(d, e, f, div)) % div)


if __name__ == "__main__":
    main()
