# ABC-420 A - What month is it?
# https://atcoder.jp/contests/abc420/tasks/abc420_a
#
def getIntMap():
    return map(int, input().split())


def main():
    X, Y = getIntMap()

    n = (X + Y) % 12

    print(12 if n == 0 else n)


if __name__ == "__main__":
    main()
