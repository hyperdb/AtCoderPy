# ABC-080 A - Parking
# https://atcoder.jp/contests/abc080/tasks/abc080_a
#
def getIntMap():
    return map(int, input().split())


def main():
    n, a, b = getIntMap()
    c = n * a

    print(c if c < b else b)


if __name__ == "__main__":
    main()
