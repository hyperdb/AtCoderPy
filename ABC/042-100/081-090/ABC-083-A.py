# ABC-083 A - Libra
# https://atcoder.jp/contests/abc083/tasks/abc083_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c, d = getIntMap()
    e = a + b
    f = c + d

    print('Balanced' if e == f else 'Left' if e > f else 'Right')


if __name__ == "__main__":
    main()
