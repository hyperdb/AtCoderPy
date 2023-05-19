# ABC-211 A - Blood Pressure
# https://atcoder.jp/contests/abc211/tasks/abc211_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    c = (a + 2 * b) / 3

    print("%d" % c if c.is_integer() else c)


if __name__ == "__main__":
    main()
