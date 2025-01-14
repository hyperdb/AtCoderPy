# ABC-386 A - Full House 2
# https://atcoder.jp/contests/abc386/tasks/abc386_a
#
def getIntMap():
    return map(int, input().split())


def main():
    A, B, C, D = getIntMap()
    c = dict()
    for i in [A, B, C, D]:
        c.setdefault(i, 0)
        c[i] += 1

    k = list(c.keys())
    v = list(c.values())
    v.sort()

    print("Yes" if len(k) == 2 and (v == [1, 3] or v == [2, 2]) else "No")


if __name__ == "__main__":
    main()
