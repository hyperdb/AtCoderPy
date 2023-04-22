# ABC-209 B - Can you buy them all?
# https://atcoder.jp/contests/abc209/tasks/abc209_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, x = getIntMap()
    a = getIntList()

    print('Yes' if x >= sum(a) - len(a) // 2 else 'No')


if __name__ == "__main__":
    main()
