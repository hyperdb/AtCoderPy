# ABC-344 C - A+B+C
# https://atcoder.jp/contests/abc344/tasks/abc344_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()
    m = getInt()
    b = getIntList()
    l = getInt()
    c = getIntList()
    q = getInt()
    x = getIntList()

    d = set()
    for i in a:
        for j in b:
            for k in c:
                d.add(i + j + k)

    for e in x:
        print('Yes' if e in d else 'No')


if __name__ == "__main__":
    main()
