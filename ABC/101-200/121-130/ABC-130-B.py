# ABC-130 B - Bounding
# https://atcoder.jp/contests/abc130/tasks/abc130_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, x = getIntMap()
    l = getIntList()

    if sum(l) <= x:
        print(len(l) + 1)
    else:
        p = 0
        b = 1

        for i in range(1, len(l)):
            p = p + l[i - 1]
            if p > x:
                break
            b += 1

        print(b)


if __name__ == "__main__":
    main()
