# ABC-337 C - Lining Up 2
# https://atcoder.jp/contests/abc337/tasks/abc337_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    if n == 1:
        print('1')
    else:
        d = dict()
        s = 0
        for i in range(n):
            if a[i] == -1:
                s = i + 1
            else:
                d[a[i]] = i + 1

        c = [s]
        while True:
            s = d[s]
            c.append(s)
            if len(c) == n:
                break

        print(" ".join(map(str, c)))


if __name__ == "__main__":
    main()
