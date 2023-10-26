# ABC-312 C - Invisible Hand
# https://atcoder.jp/contests/abc312/tasks/abc312_c
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def check(a, b, p):
    sellers = len([x for x in a if x <= p])
    buyers = len([x for x in b if x >= p])
    return sellers >= buyers


def main():
    n, m = getIntMap()
    a = getIntList()
    b = getIntList()

    p = list(set(a + [x + 1 for x in b]))
    p.sort()

    while True:

        midP = (min(p) + max(p)) // 2

        if not check(a, b, midP):
            p = [x for x in p if x > midP]
        else:
            p = [x for x in p if x <= midP]

        if len(p) == 1:
            print(p[0])
            break


if __name__ == "__main__":
    main()
