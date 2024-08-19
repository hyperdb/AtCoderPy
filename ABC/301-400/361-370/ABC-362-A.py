# ABC-362 A - Buy a Pen
# https://atcoder.jp/contests/abc362/tasks/abc362_a
#
def getIntList():
    return list(map(int, input().split()))


def getString():
    return input()


def main():
    RGB = getIntList()
    C = getString()

    cname = ["Red", "Green", "Blue"]
    x = cname.index(C)
    RGB[x] = 100

    print(min(RGB))


if __name__ == "__main__":
    main()
