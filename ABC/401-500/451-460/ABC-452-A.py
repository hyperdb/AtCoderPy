# ABC-452 A - Gothec
# https://atcoder.jp/contests/abc452/tasks/abc452_a
#
def getIntMap():
    return map(int, input().split())


def main():
    M, D = getIntMap()
    sekku = [(1, 7), (3, 3), (5, 5), (7, 7), (9, 9)]

    print("Yes" if (M, D) in sekku else "No")


if __name__ == "__main__":
    main()
