# ABC-088 B - Card Game for Two
# https://atcoder.jp/contests/abc088/tasks/abc088_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    a.sort()
    a.reverse()

    r = 0
    for i in range(len(a)):
        r += a[i] if i % 2 == 0 else a[i] * - 1
    print(r)


if __name__ == "__main__":
    main()
