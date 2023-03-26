# ABC-182 B - Almost GCD
# https://atcoder.jp/contests/abc182/tasks/abc182_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    b = 0
    c = 0
    for i in range(2, max(a) + 1):
        d = len([t for t in a if t % i == 0])
        if d >= c:
            c = d
            b = i
        if d == len(a):
            break
    print(b)


if __name__ == "__main__":
    main()
