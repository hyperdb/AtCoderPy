# ABC-072 A - Sandglass2
# https://atcoder.jp/contests/abc072/tasks/abc072_a
#
def getIntMap():
    return map(int, input().split())


def main():
    x, t = getIntMap()

    r = x - t
    print(r if r >= 0 else 0)


if __name__ == "__main__":
    main()
