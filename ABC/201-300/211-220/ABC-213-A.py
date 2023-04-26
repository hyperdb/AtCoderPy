# ABC-213 A - Bitwise Exclusive Or
# https://atcoder.jp/contests/abc213/tasks/abc213_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(a ^ b)


if __name__ == "__main__":
    main()
