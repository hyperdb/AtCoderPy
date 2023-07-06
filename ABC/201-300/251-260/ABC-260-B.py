# ABC-260 B - Better Students Are Needed!
# https://atcoder.jp/contests/abc260/tasks/abc260_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def toDict(l):
    temp = {}
    for i in range(len(l)):
        temp[i] = l[i]
    return temp


def sortDict(d):
    return sorted(d.items(), key=lambda p: p[1], reverse=True)


def selectDict(passed, target, all, lim):
    for i in range(all):
        if len(passed) >= lim:
            break
        m = target[i][0]
        if not m in passed:
            passed.append(m)
    return passed


def main():
    n, x, y, z = getIntMap()
    a = getIntList()
    b = getIntList()
    c = [a[i] + b[i] for i in range(n)]

    aa = toDict(a)
    bb = toDict(b)
    cc = toDict(c)

    aa = sortDict(aa)
    bb = sortDict(bb)
    cc = sortDict(cc)

    d = []
    d = selectDict(d, aa, n, x)
    d = selectDict(d, bb, n, x + y)
    d = selectDict(d, cc, n, x + y + z)

    d.sort()
    for i in d:
        print(i + 1)


if __name__ == "__main__":
    main()
