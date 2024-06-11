# ABC-047 A - キャンディーと2人の子供
# https://atcoder.jp/contests/abc047/tasks/abc047_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    d = getIntList()
    d.sort()

    print('Yes' if d[2] == d[0] + d[1] else 'No')


if __name__ == "__main__":
    main()
