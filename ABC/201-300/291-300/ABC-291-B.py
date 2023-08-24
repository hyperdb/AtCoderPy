# ABC-291 B - Trimmed Mean
# https://atcoder.jp/contests/abc291/tasks/abc291_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    x = getIntList()

    x.sort()
    y = x[n:n*4]

    print(sum(y) / (3 * n))


if __name__ == "__main__":
    main()
