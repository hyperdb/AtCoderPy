# ABC-201 A - Tiny Arithmetic Sequence
# https://atcoder.jp/contests/abc201/tasks/abc201_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    l = getIntList()
    a, b, c = sorted(l)

    print('Yes' if b * 2 == a + c else 'No')


if __name__ == "__main__":
    main()
