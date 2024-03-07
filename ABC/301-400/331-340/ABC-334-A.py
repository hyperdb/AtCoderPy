# ABC-334 A - Christmas Present
# https://atcoder.jp/contests/abc334/tasks/abc334_a
#
def getIntMap():
    return map(int, input().split())


def main():
    b, g = getIntMap()

    print('Bat' if b > g else 'Glove')


if __name__ == "__main__":
    main()
