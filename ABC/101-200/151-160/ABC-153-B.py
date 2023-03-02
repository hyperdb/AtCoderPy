# ABC-153 B - Common Raccoon vs Monster
# https://atcoder.jp/contests/abc153/tasks/abc153_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    h, n = getIntMap()
    a = getIntList()

    print('Yes' if h <= sum(a) else 'No')


if __name__ == "__main__":
    main()
