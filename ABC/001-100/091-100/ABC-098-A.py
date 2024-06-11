# ABC-098 A - Add Sub Mul
# https://atcoder.jp/contests/abc098/tasks/abc098_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(max([a + b, a - b, a * b]))


if __name__ == "__main__":
    main()
