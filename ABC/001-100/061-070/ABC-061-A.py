# ABC-061 A - Between Two Integers
# https://atcoder.jp/contests/abc061/tasks/abc061_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()
    print('Yes' if a <= c and c <= b else 'No')


if __name__ == "__main__":
    main()
