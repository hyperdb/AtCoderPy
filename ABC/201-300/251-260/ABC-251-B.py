# ABC-251 B - At Most 3 (Judge ver.)
# https://atcoder.jp/contests/abc251/tasks/abc251_b
#
import itertools


def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, w = getIntMap()
    a = getIntList()

    b = []
    for i in range(3):
        for c in itertools.combinations(a, i + 1):
            d = sum(c)
            if d <= w:
                b.append(d)

    print(len(set(b)))


if __name__ == "__main__":
    main()
