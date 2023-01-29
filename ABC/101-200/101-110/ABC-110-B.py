# ABC-110 B - 1 Dimensional World's Tale
# https://atcoder.jp/contests/abc110/tasks/abc110_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, m, x, y = getIntMap()
    X = max(getIntList())
    Y = min(getIntList())

    r = False
    for z in range(x + 1, y + 1):
        if X < z and Y >= z:
            r = True
            break
    print('No War' if r else 'War')


if __name__ == "__main__":
    main()
