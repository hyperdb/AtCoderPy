# ABC-384 C - Perfect Standings
# https://atcoder.jp/contests/abc384/tasks/abc384_c
#
import itertools


def getIntList():
    return list(map(int, input().split()))


def main():
    point = getIntList()

    q = [i for i in range(5)]

    c = []
    for i in range(5):
        c += list(itertools.combinations(q, i + 1))

    k = dict()
    for arr in c:
        s = ""
        t = 0
        for x in arr:
            s += chr(ord("A") + x)
            t += point[x]
        k.setdefault(t, set())
        k[t].add(s)
    sk = sorted(k.keys())
    sk.reverse()

    for key in sk:
        items = sorted(k[key])
        for item in items:
            print(item)


if __name__ == "__main__":
    main()
