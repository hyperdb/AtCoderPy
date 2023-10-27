# ABC-313 C - Approximate Equalization 2
# https://atcoder.jp/contests/abc313/tasks/abc313_c
#
def getInt():
    return int(input())


def getIntList():
    return list(map(int, input().split()))


def main():
    n = getInt()
    a = getIntList()

    if n == 1:
        print(0)
    else:
        a.sort()

        dv, md = divmod(sum(a), n)
        ave = [dv for _ in range(n)]

        for i in range(md):
            ave[-1 * (i + 1)] += 1

        print(sum([abs(ave[i] - a[i]) for i in range(n)]) // 2)


if __name__ == "__main__":
    main()
