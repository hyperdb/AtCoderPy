# ABC-129 B - Balance
# https://atcoder.jp/contests/abc129/tasks/abc129_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    w = getIntList()

    t = sum(w)

    s1 = 0
    s2 = 0
    a = t
    for i in w:
        s1 += i
        s2 = t - s1
        b = abs(s1 - s2)
        a = a if b > a else b
        if s1 > s2:
            break

    print(a)


if __name__ == "__main__":
    main()
