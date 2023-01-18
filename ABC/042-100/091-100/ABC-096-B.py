# ABC-096 B - Maximum Sum
# https://atcoder.jp/contests/abc096/tasks/abc096_b
#
def getIntList():
    return list(map(int, input().split()))


def getInt():
    return int(input())


def main():
    n = getIntList()
    k = getInt()

    n.sort()
    n.reverse()

    for i in range(k):
        n[0] = n[0] * 2

    print(sum(n))


if __name__ == "__main__":
    main()
