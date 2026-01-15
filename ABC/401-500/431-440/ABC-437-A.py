# A - Feet
# https://atcoder.jp/contests/abc437/tasks/abc437_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B = getIntMap()

    print(A * 12 + B)


if __name__ == "__main__":
    main()
