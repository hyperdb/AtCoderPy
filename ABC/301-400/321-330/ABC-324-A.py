# ABC-324 A - Same
# https://atcoder.jp/contests/abc324/tasks/abc324_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    print('Yes' if len(set(a)) == 1 else 'No')


if __name__ == "__main__":
    main()
