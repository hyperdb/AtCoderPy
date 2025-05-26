# ABC-406 B - Product Calculator
# https://atcoder.jp/contests/abc406/tasks/abc406_b
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    N, K = getIntMap()
    A = getIntList()

    d = 1
    for i in range(N):
        d *= A[i]
        if d >= 10**K:
            d = 1
    print(d)


if __name__ == "__main__":
    main()
