# ABC-205 A - kcal
# https://atcoder.jp/contests/abc205/tasks/abc205_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    c = b / 100 * a
    print("%d" % c if c.is_integer() else c)


if __name__ == "__main__":
    main()
