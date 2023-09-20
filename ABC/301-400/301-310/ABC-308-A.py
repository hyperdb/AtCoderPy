# ABC-308 A - New Scheme
# https://atcoder.jp/contests/abc308/tasks/abc308_a
#
def getIntList():
    return list(map(int, input().split()))


def main():
    a = getIntList()
    b = [1 for i in range(1, len(a)) if a[i] < a[i - 1]]
    c = [a[i] % 25 for i in range(len(a))]

    r = True
    if min(a) < 100 or max(a) > 675:
        r = False
    elif len(b) > 0:
        r = False
    elif sum(c) > 0:
        r = False

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
