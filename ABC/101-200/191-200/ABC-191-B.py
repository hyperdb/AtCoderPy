# ABC-191 B - Remove It
# https://atcoder.jp/contests/abc191/tasks/abc191_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, x = getIntMap()
    a = getIntList()

    b = [str(i) for i in a if i != x]

    print(" ".join(b))


if __name__ == "__main__":
    main()
