# ABC042 A - 和風いろはちゃんイージー
# https://atcoder.jp/contests/abc042/tasks/abc042_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    d = getIntList()
    d.sort()

    if d == [5, 5, 7]:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
