# ABC-257 B - 1D Pawn
# https://atcoder.jp/contests/abc257/tasks/abc257_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k, q = getIntMap()
    a = getIntList()
    l = getIntList()

    for x in l:
        p = a[x - 1]
        if p == n or p + 1 in a:
            continue
        else:
            a[x - 1] += 1

    print(" ".join(map(str, a)))


if __name__ == "__main__":
    main()
