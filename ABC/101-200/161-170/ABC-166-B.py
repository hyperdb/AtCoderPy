# ABC-166 B - Trick or Treat
# https://atcoder.jp/contests/abc166/tasks/abc166_b
#
def getIntMap():
    return map(int, input().split())


def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k = getIntMap()

    s = [i + 1 for i in range(n)]

    for i in range(k):
        d = getInt()
        a = getIntList()
        for j in a:
            if j in s:
                s.remove(j)
    print(len(s))


if __name__ == "__main__":
    main()
