# ABC-171 B - Mix Juice
# https://atcoder.jp/contests/abc171/tasks/abc171_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, m = getIntMap()
    p = getIntList()

    p.sort()

    s = 0
    for i in range(m):
        s += p[i]
    print(s)


if __name__ == "__main__":
    main()
