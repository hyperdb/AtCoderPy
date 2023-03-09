# ABC-161 B - Popular Vote
# https://atcoder.jp/contests/abc161/tasks/abc161_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, m = getIntMap()
    a = getIntList()

    c = 0
    l = sum(a) / (4 * m)

    for x in a:
        if x >= l:
            c += 1
            if c == m:
                break

    print('Yes' if c == m else 'No')


if __name__ == "__main__":
    main()
