# ABC-311 A - First ABC
# https://atcoder.jp/contests/abc311/tasks/abc311_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = [''] + list(getString())

    print(max([s.index('A'), s.index('B'), s.index('C')]))


if __name__ == "__main__":
    main()
