# ABC-330 B - Minimize Abs 1
# https://atcoder.jp/contests/abc330/tasks/abc330_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, l, r = getIntMap()
    a = getIntList()

    b = []
    for i in a:
        x = i
        if i < l:
            x = l
        elif i > r:
            x = r
        b.append(x)
    print(" ".join(list(map(str, b))))


if __name__ == "__main__":
    main()
