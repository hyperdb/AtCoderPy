# ABC-328 B - 11/11
# https://atcoder.jp/contests/abc328/tasks/abc328_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    d = [0] + getIntList()

    c = 0
    for i in range(1, n + 1):
        for j in range(1, d[i] + 1):
            if len(set(list("%d%d" % (i, j)))) == 1:
                c += 1
    print(c)


if __name__ == "__main__":
    main()
