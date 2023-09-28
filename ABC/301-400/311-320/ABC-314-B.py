# ABC-314 B - Roulette
# https://atcoder.jp/contests/abc314/tasks/abc314_b
#
def getInt():
    return int(input())

def getIntList():
    return list(map(int, input().split()))

def main():
    n = getInt()
    c = []
    a = [[]]

    for i in range(n):
        c.append(getInt())
        a.append(getIntList())

    x = getInt()
    b = {}
    m = 99
    for i in range(n + 1):
        if x in a[i]:
            b[i] = len(a[i])
            m = min(m, len(a[i]))
    r = []
    for x in b.keys():
        if b[x] == m:
            r.append(x)

    print(len(r))
    print(" ".join(map(str, r)))

if __name__ == "__main__":
    main()