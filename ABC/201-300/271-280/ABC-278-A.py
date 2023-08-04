# ABC-278 A - Shift
# https://atcoder.jp/contests/abc278/tasks/abc278_a
#
def getIntMap():
    return map(int, input().split())


def getStringList():
    return list(input().split())


def s(x):
    return [x[i] for i in range(1, len(x))] + ['0']


def main():
    n, k = getIntMap()
    a = getStringList()

    for i in range(k):
        a = s(a)
    print(' '.join(a))


if __name__ == "__main__":
    main()
