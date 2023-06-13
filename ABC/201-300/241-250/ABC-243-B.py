# ABC-243 B - Hit and Blow
# https://atcoder.jp/contests/abc243/tasks/abc243_b
#
def getInt():
    return int(input())

def getIntList():
    return list(map(int, input().split()))

def main():
    n = getInt()
    a = getIntList()
    b = getIntList()

    c1 = len([a[i] for i in range(len(a)) if a[i] == b[i]])
    c2 = len([a[i] for i in range(len(a)) if a[i] in b])

    print(c1)
    print(c2 - c1)


if __name__ == "__main__":
    main()