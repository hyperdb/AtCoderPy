# ABC-346 C - Σ
# https://atcoder.jp/contests/abc346/tasks/abc346_c
#
def getIntMap():
    return map(int, input().split())


def getIntList():
    return list(map(int, input().split()))


def main():
    n, k = getIntMap()
    a = getIntList()

    b = [i for i in set(a) if i <= k]

    c = ((1 + k) * k) // 2

    print(c - sum(b))


if __name__ == "__main__":
    main()
