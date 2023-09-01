# ABC-297 A - Double Click
# https://atcoder.jp/contests/abc297/tasks/abc297_a
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, d = getIntMap()
    t = getIntList()

    c = [i for i in range(1, n) if t[i] - t[i - 1] <= d]

    print(t[min(c)] if len(c) > 0 else -1)


if __name__ == "__main__":
    main()
