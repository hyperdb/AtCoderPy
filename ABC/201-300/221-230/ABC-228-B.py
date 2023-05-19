# ABC-228 B - Takahashi's Secret
# https://atcoder.jp/contests/abc228/tasks/abc228_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, x = getIntMap()
    a = getIntList()
    f = [False for _ in range(n)]

    i = x - 1
    while f[i] == False:
        f[i] = True
        i = a[i] - 1
    print(f.count(True))


if __name__ == "__main__":
    main()
