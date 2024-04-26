# ABC-339 C - Perfect Bus
# https://atcoder.jp/contests/abc339/tasks/abc339_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    p = 0
    b = [p]
    for x in a:
        p += x
        b.append(p)

    d = min(b)
    r = b[-1]
    print(r if d >= 0 else r - d)

if __name__ == "__main__":
    main()
