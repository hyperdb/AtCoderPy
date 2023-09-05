# ABC-299 B - Trick Taking
# https://atcoder.jp/contests/abc299/tasks/abc299_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, t = getIntMap()
    c = [0] + getIntList()
    r = [0] + getIntList()

    a = [i for i in range(len(c)) if c[i] == t]

    if len(a) == 0:
        a = [i for i in range(len(c)) if c[i] == c[1]]

    x = max([r[i] for i in a])
    print(r.index(x))


if __name__ == "__main__":
    main()
