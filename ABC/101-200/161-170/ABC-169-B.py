# ABC-169 B - Multiplication 2
# https://atcoder.jp/contests/abc169/tasks/abc169_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    if 0 in a:
        print(0)
    else:
        m = 10**18
        c = a[0]
        for i in range(1, len(a)):
            c *= a[i]
            if c > m:
                c = -1
                break
        print(c)


if __name__ == "__main__":
    main()
