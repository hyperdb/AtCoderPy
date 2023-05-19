# ABC-129 A - Airplane
# https://atcoder.jp/contests/abc129/tasks/abc129_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    l = getIntList()
    l.sort()

    print(l[0] + l[1])


if __name__ == "__main__":
    main()
