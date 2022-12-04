# ABC042 A - 和風いろはちゃんイージー
# https://atcoder.jp/contests/abc042/tasks/abc042_a
#
def getIntList():
    return list(map(int, input().split()))


def main():

    l = getIntList()
    l.sort()

    if (l == [5, 5, 7]):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
