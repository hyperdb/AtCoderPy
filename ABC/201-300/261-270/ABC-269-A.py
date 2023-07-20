# ABC-269 A - Anyway Takahashi
# https://atcoder.jp/contests/abc269/tasks/abc269_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b, c, d = getIntMap()

    print((a + b) * (c - d))
    print('Takahashi')


if __name__ == "__main__":
    main()
