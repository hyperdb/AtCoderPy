# ABC-100 A - Happy Birthday!
# https://atcoder.jp/contests/abc100/tasks/abc100_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print('Yay!' if a <= 8 and b <= 8 else ':(')


if __name__ == "__main__":
    main()
