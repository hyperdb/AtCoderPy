# ABC-363 B - Japanese Cursed Doll
# https://atcoder.jp/contests/abc363/tasks/abc363_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, T, P = getIntMap()
    L = getIntList()
    L.sort()
    L.reverse()

    x = L[P - 1]
    print(0 if x >= T else T - x)


if __name__ == "__main__":
    main()
