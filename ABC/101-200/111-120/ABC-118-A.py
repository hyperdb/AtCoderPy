# ABC-118 A - B +/- A
# https://atcoder.jp/contests/abc118/tasks/abc118_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(a + b if b % a == 0 else b - a)


if __name__ == "__main__":
    main()
