# ABC-440 A - Octave
# https://atcoder.jp/contests/abc440/tasks/abc440_a
#
def getIntMap():
    return map(int, input().split())


def main():
    X, Y = getIntMap()

    print(X * 2**Y)


if __name__ == "__main__":
    main()
