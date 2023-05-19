# ABC-221 A - Seismic magnitude scales
# https://atcoder.jp/contests/abc221/tasks/abc221_a
#
def getIntMap():
    return map(int, input().split())


def main():
    a, b = getIntMap()

    print(32 ** (a - b))


if __name__ == "__main__":
    main()
