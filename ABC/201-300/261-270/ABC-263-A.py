# ABC-263 A - Full House
# https://atcoder.jp/contests/abc263/tasks/abc263_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    a = getIntList()
    b = list(set(a))

    print('Yes' if len(b) == 2 and 2 <= a.count(b[0]) <= 3 else 'No')


if __name__ == "__main__":
    main()
