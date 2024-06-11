# ABC-078 A - HEX
# https://atcoder.jp/contests/abc078/tasks/abc078_a
#
def getStringMap():
    return input().split()


def main():
    x, y = getStringMap()
    print('=' if x == y else '<' if x < y else '>')


if __name__ == "__main__":
    main()
