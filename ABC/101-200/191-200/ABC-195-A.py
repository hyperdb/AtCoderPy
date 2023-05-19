# ABC-195 A - Health M Death
# https://atcoder.jp/contests/abc195/tasks/abc195_a
#
def getIntMap():
    return map(int, input().split())


def main():
    m, n = getIntMap()

    print('Yes' if n % m == 0 else 'No')


if __name__ == "__main__":
    main()
