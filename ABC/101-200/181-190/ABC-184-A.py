# ABC-184 A - Determinant
# https://atcoder.jp/contests/abc184/tasks/abc184_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()
    c, d = getIntMap()

    print(a * d - b * c)


if __name__ == "__main__":
    main()
