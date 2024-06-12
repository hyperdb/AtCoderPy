# ABC-040 A - 赤赤赤赤青
# https://atcoder.jp/contests/abc040/tasks/abc040_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, x = getIntMap()

    print(min(n - x, x - 1))


if __name__ == "__main__":
    main()
