# ABC-154 A - Remaining Balls
# https://atcoder.jp/contests/abc154/tasks/abc154_a
#
def getStringMap():
    return input().split()


def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    s, t = getStringMap()
    a, b = getIntMap()
    u = getString()

    a, b = [a, b - 1] if u == t else [a - 1, b]

    print('%d %d' % (a, b))


if __name__ == "__main__":
    main()
