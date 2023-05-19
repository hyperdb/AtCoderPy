# ABC-143 A - Curtain
# https://atcoder.jp/contests/abc143/tasks/abc143_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    c = a - 2 * b
    print(c if c >= 0 else 0)


if __name__ == "__main__":
    main()
