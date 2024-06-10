# ABC-355 B - Piano 2
# https://atcoder.jp/contests/abc355/tasks/abc355_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, m = getIntMap()
    a = getIntList()
    b = getIntList()

    c = dict()
    for i in a:
        c[i] = 'A'
    for i in b:
        c[i] = 'B'

    d = ''
    for k in sorted(c.keys()):
        d += c[k]

    if d.find('AA') >= 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
