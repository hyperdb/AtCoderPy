# ABC-289 B - レ
# https://atcoder.jp/contests/abc289/tasks/abc289_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, m = getIntMap()
    if m > 0:
        a = getIntList()

    l = [i + 1 for i in range(n)]
    if m == 0:
        print(" ".join(map(str, l)))
    else:
        b = []
        c = []
        for x in l:
            b.append(x)
            if not x in a:
                b.reverse()
                c += b
                b = []
        print(" ".join(map(str, c)))


if __name__ == "__main__":
    main()
