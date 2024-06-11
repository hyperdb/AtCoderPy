# ABC-060 A - Shiritori
# https://atcoder.jp/contests/abc060/tasks/abc060_a
#
def getStringMap():
    return input().split()


def main():
    a, b, c = getStringMap()

    print('YES' if a[-1] == b[0] and b[-1] == c[0] else 'NO')


if __name__ == "__main__":
    main()
