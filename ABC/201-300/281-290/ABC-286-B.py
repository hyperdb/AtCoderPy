# ABC-286 B - Cat
# https://atcoder.jp/contests/abc286/tasks/abc286_b
#
import re


def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = getString()

    print(re.sub('na', 'nya', s))


if __name__ == "__main__":
    main()
