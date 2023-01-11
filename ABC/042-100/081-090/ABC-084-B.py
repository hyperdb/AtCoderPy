# ABC-084 B - Postal Code
# https://atcoder.jp/contests/abc084/tasks/abc084_b
#
import re


def getIntMap():
    return map(int, input().split())


def getString():
    return input()


def main():
    a, b = getIntMap()
    s = getString()

    c = r'[0-9]{' + str(a) + '}-[0-9]{' + str(b) + '}'
    m = re.match(c, s)

    print('Yes' if not m is None else 'No')


if __name__ == "__main__":
    main()
