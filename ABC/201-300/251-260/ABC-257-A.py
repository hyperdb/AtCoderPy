# ABC-257 A - A to Z String 2
# https://atcoder.jp/contests/abc257/tasks/abc257_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, x = getIntMap()

    print(chr(ord('A') + (x - 1) // n))


if __name__ == "__main__":
    main()
