# ABC-074 B - Collecting Balls (Easy Version)
# https://atcoder.jp/contests/abc074/tasks/abc074_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    k = getInt()
    x = getIntList()

    r = 0
    for i in range(n):
        r += (x[i] if x[i] * 2 < k else (k - x[i])) * 2
    print(r)


if __name__ == "__main__":
    main()
