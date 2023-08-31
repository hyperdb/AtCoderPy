# ABC-296 A - Alternately
# https://atcoder.jp/contests/abc296/tasks/abc296_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = getString()

    print('Yes' if s.find('MM') == -1 and s.find('FF') == -1 else 'No')


if __name__ == "__main__":
    main()
