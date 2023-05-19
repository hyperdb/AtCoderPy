# ABC-130 A - Rounding
# https://atcoder.jp/contests/abc130/tasks/abc130_a
#
def getIntMap():
    return map(int, input().split())


def main():
    x, a = getIntMap()

    print(0 if x < a else 10)


if __name__ == "__main__":
    main()
