# ABC-094 A - Cats and Dogs
# https://atcoder.jp/contests/abc094/tasks/abc094_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, x = getIntMap()

    print('YES' if x >= a and x - a <= b else 'NO')


if __name__ == "__main__":
    main()
