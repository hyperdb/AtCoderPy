# ABC-064 A - RGB Cards
# https://atcoder.jp/contests/abc064/tasks/abc064_a
#
def getIntMap():
    return map(int, input().split())


def main():
    r, g, b = getIntMap()

    print('YES' if ((r * 100 + g * 10 + b) % 4) == 0 else 'NO')


if __name__ == "__main__":
    main()
