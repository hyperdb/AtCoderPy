# ABC-113 B - Palace
# https://atcoder.jp/contests/abc113/tasks/abc113_b
#
def getInt():
    return int(input())


def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    t, a = getIntMap()
    h = getIntList()

    x = []
    for i in range(len(h)):
        y = abs((t - h[i] * 0.006) - a)
        x.append([y, i + 1])

    x.sort()

    print(x[0][1])


if __name__ == "__main__":
    main()
