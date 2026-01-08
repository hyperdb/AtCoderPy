# ABC-434 A - Balloon Trip
# https://atcoder.jp/contests/abc434/tasks/abc434_a
#
def getIntMap():
    return map(int, input().split())


def main():
    W, B = getIntMap()

    print((W * 1000) // B + 1)


if __name__ == "__main__":
    main()
