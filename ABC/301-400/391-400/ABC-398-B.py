# ABC-398 B - Full House 3
# https://atcoder.jp/contests/abc398/tasks/abc398_b
#
def getIntList():
    return list(map(int, input().split()))


def main():
    A = getIntList()

    d = dict()
    for n in A:
        d.setdefault(n, 0)
        d[n] += 1

    c = []
    for x in d.keys():
        if d[x] >= 2:
            c.append(d[x])

    print("Yes" if len(c) >= 2 and max(c) >= 3 else "No")


if __name__ == "__main__":
    main()
