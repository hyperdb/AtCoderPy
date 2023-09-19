# ABC-307 A - Weekly Records
# https://atcoder.jp/contests/abc307/tasks/abc307_a
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    sw = []
    for i in range(n):
        s = i * 7
        e = s + 7
        sw.append(sum(a[s:e]))

    print(" ".join(map(str, sw)))


if __name__ == "__main__":
    main()
