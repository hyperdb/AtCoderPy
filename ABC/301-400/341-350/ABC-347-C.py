# ABC-347 C - Ideal Holidays
# https://atcoder.jp/contests/abc347/tasks/abc347_c
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, a, b = getIntMap()
    d = getIntList()

    wd = a + b
    d = [x % wd for x in d]
    d = list(set(d))
    d.sort()

    r = False
    c = len(d)
    for i in range(c):
        d.append(d[i] + wd)
        s = i
        e = i + c - 1

        if d[e] - d[s] < a:
            r = True

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
