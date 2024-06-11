# ABC-054 A - One Card Poker
# https://atcoder.jp/contests/abc054/tasks/abc054_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()
    p = [0, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    print('Draw' if a == b else 'Alice' if p[a] > p[b] else 'Bob')


if __name__ == "__main__":
    main()
