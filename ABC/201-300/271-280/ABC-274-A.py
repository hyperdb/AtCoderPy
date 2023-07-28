# ABC-274 A - Batting Average
# https://atcoder.jp/contests/abc274/tasks/abc274_a
#
def getIntMap():
    return map(int, input().split())


def r(x):
    return '1.000' if x == 1.0 else "0.%03d" % ((x * 10000 + 5) // 10)


def main():
    a, b = getIntMap()

    print(r(b / a))


if __name__ == "__main__":
    main()
