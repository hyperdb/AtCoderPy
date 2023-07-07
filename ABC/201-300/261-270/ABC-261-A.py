# ABC-261 A - Intersection
# https://atcoder.jp/contests/abc261/tasks/abc261_a
#
def getIntMap():
    return map(int, input().split())


def main():
    l1, r1, l2, r2 = getIntMap()

    ln = min(r1, r2) - max(l1, l2)

    print(ln if ln >= 0 else 0)


if __name__ == "__main__":
    main()
