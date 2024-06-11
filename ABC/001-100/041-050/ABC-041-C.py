# ABC-041 C - 背の順
# https://atcoder.jp/contests/abc041/tasks/abc041_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    N = getInt()
    a = getIntList()

    b = {}
    for i in range(N):
        b[a[i]] = i + 1

    c = [b[k] for k in sorted(b.keys())]
    c.reverse()

    for x in c:
        print(x)


if __name__ == "__main__":
    main()
