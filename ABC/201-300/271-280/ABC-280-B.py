# ABC-280 B - Inverse Prefix Sum
# https://atcoder.jp/contests/abc280/tasks/abc280_b
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    s = getIntList()
    a = []

    for i in range(len(s)):
        if i == 0:
            x = s[i]
        else:
            x = s[i] - sum(a)
        a.append(x)

    print(" ".join(list(map(str, a))))


if __name__ == "__main__":
    main()
