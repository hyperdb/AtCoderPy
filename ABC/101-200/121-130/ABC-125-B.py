# ABC-125 B - Resale
# https://atcoder.jp/contests/abc125/tasks/abc125_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    v = getIntList()
    c = getIntList()

    r = 0
    for i in range(len(v)):
        x = v[i] - c[i]
        r += x if x > 0 else 0
    print(r)


if __name__ == "__main__":
    main()
