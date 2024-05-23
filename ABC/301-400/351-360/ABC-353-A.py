# ABC-353 A - Buildings
# https://atcoder.jp/contests/abc353/tasks/abc353_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    r = -1
    for i in range(1, n):
        if a[i] > a[0]:
            r = (i + 1)
            break
    print(r)


if __name__ == "__main__":
    main()
