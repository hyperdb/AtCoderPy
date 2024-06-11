# ABC-057 A - Remaining Time
# https://atcoder.jp/contests/abc057/tasks/abc057_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print((a + b) % 24)


if __name__ == "__main__":
    main()
