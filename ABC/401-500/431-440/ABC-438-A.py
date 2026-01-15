# ABC-438 A - First Contest of the Year
# https://atcoder.jp/contests/abc438/tasks/abc438_a
#
def getIntMap():
    return map(int, input().split())


def main():
    D, F = getIntMap()

    result = (F - (D % 7)) % 7

    print(result if result != 0 else 7)


if __name__ == "__main__":
    main()
