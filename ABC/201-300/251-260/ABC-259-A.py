# ABC-259 A - Growth Record
# https://atcoder.jp/contests/abc259/tasks/abc259_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, m, x, t, d = getIntMap()

    print(t if m >= x else t - (x - m) * d)


if __name__ == "__main__":
    main()
