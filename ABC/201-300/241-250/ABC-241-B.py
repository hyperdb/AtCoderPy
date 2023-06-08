# ABC-241 B - Pasta
# https://atcoder.jp/contests/abc241/tasks/abc241_b
#
def getIntMap():
    return map(int, input().split())

def getIntList():
    return list(map(int, input().split()))

def main():
    n, m = getIntMap()
    a = getIntList()
    b = getIntList()

    c = {}
    for x in a:
        if not x in c:
            c.setdefault(x, 0)
        c[x] += 1

    for y in b:
        if not y in c:
            c.setdefault(y, 0)
        c[y] -= 1

    print('Yes' if min(c.values()) >= 0 else 'No')

if __name__ == "__main__":
    main()