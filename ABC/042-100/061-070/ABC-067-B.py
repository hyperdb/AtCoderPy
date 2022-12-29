# ABC-067 B - Snake Toy
# https://atcoder.jp/contests/abc067/tasks/abc067_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k = getIntMap()
    l = getIntList()

    d = sorted(l, reverse=True)

    print(sum(d[:k]))


if __name__ == "__main__":
    main()
