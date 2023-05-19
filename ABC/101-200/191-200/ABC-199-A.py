# ABC-199 A - Square Inequality
# https://atcoder.jp/contests/abc199/tasks/abc199_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c = getIntMap()

    print('Yes' if a ** 2 + b ** 2 < c ** 2 else 'No')


if __name__ == "__main__":
    main()
