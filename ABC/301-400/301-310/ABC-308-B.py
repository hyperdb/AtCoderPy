# ABC-308 B - Default Price
# https://atcoder.jp/contests/abc308/tasks/abc308_b
#
def getIntMap():
    return map(int, input().split())


def getStringList():
    return list(input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, m = getIntMap()
    c = getStringList()
    d = [''] + getStringList()
    p = getIntList()

    t = 0
    for cx in c:
        dx = 0 if cx not in d else d.index(cx)
        t += p[dx]
    print(t)


if __name__ == "__main__":
    main()
