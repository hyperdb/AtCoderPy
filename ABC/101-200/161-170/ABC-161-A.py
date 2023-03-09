# ABC-161 A - ABC Swap
# https://atcoder.jp/contests/abc161/tasks/abc161_a
#
def getIntMap():
    return map(int, input().split())


def swap(a, b):
    return b, a


def main():
    x, y, z = getIntMap()

    x, y = swap(x, y)
    x, z = swap(x, z)

    print('%d %d %d' % (x, y, z))


if __name__ == "__main__":
    main()
