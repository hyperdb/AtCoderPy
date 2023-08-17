# ABC-286 A - Range Swap
# https://atcoder.jp/contests/abc286/tasks/abc286_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, p, q, r, s = getIntMap()
    a = getIntList()
    c = [i for i in range(n)]

    i = 0
    for x in range(p - 1, q):
        c[x] = (r - 1) + i
        i += 1
    i = 0
    for x in range(r - 1, s):
        c[x] = (p - 1) + i
        i += 1

    b = [a[i] for i in c]

    print(' '.join(list(map(str, b))))


if __name__ == "__main__":
    main()
