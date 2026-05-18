# ABC-456 B - 456
# https://atcoder.jp/contests/abc456/tasks/abc456_b
#
def getIntList():
    return list(map(int, input().split()))


def main():
    A = getIntList()
    B = getIntList()
    C = getIntList()

    All = 6 * 6 * 6
    match = 0
    for a in A:
        for b in B:
            for c in C:
                if sorted([a, b, c]) == [4, 5, 6]:
                    match += 1

    print(match / All)


if __name__ == "__main__":
    main()
