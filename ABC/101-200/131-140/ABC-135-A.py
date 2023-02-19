# ABC-135 A - Harmony
# https://atcoder.jp/contests/abc135/tasks/abc135_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print((a + b) // 2 if (a + b) % 2 == 0 else 'IMPOSSIBLE')


if __name__ == "__main__":
    main()
