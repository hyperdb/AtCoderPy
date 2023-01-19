# ABC-097 A - Colorful Transceivers
# https://atcoder.jp/contests/abc097/tasks/abc097_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c, d = getIntMap()

    print('Yes' if abs(a - c) <= d or (abs(a - b)
          <= d and abs(c - b) <= d) else 'No')


if __name__ == "__main__":
    main()
