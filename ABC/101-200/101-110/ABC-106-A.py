# ABC-106 A - Garden
# https://atcoder.jp/contests/abc106/tasks/abc106_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print((a - 1) * (b - 1))


if __name__ == "__main__":
    main()
