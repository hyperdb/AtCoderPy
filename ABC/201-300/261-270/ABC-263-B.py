# ABC-263 B - Ancestor
# https://atcoder.jp/contests/abc263/tasks/abc263_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    p = [0, 0] + getIntList()

    i = p[n]
    c = 1
    while i > 1:
        i = p[i]
        c += 1
    print(c)


if __name__ == "__main__":
    main()
