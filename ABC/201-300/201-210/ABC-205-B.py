# ABC-205 B - Permutation Check
# https://atcoder.jp/contests/abc205/tasks/abc205_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()
    a.sort()
    b = [i + 1 for i in range(n)]

    print('Yes' if a == b else 'No')


if __name__ == "__main__":
    main()
