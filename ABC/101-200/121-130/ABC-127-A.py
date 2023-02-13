# ABC-127 A - Ferris Wheel
# https://atcoder.jp/contests/abc127/tasks/abc127_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(0 if a <= 5 else b // 2 if a <= 12 else b)


if __name__ == "__main__":
    main()
