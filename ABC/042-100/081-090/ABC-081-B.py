# ABC-081 B - Shift only
# https://atcoder.jp/contests/abc081/tasks/abc081_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def mod(l):
    return sum(list(map(lambda x: x % 2, l)))


def div(l):
    return list(map(lambda x: x // 2, l))


def main():
    n = getInt()
    a = getIntList()

    c = 0
    while True:
        if mod(a) > 0:
            break
        a = div(a)
        c += 1
    print(c)


if __name__ == "__main__":
    main()
