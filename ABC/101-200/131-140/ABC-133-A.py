# ABC-133 A - T or T
# https://atcoder.jp/contests/abc133/tasks/abc133_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, a, b = getIntMap()

    c = n * a

    print(c if c < b else b)


if __name__ == "__main__":
    main()
