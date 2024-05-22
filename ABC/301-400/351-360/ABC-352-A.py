# ABC-352 A - AtCoder Line
# https://atcoder.jp/contests/abc352/tasks/abc352_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, x, y, z = getIntMap()

    print('Yes' if min(x, y) <= z <= max(x, y) else 'No')


if __name__ == "__main__":
    main()
