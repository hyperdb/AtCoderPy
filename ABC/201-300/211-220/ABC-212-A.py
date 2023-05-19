# ABC-212 A - Alloy
# https://atcoder.jp/contests/abc212/tasks/abc212_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print('Alloy' if a > 0 and b > 0 else 'Gold' if b == 0 else 'Silver')


if __name__ == "__main__":
    main()
