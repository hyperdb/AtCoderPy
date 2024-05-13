# ABC-333 C - Repunit Trio
# https://atcoder.jp/contests/abc333/tasks/abc333_c
#
def getInt():
    return int(input())


def main():
    n = getInt()

    mx = 13
    a = set()
    for i in range(1, mx):
        si = int('1' * i)
        for j in range(1, mx):
            sj = int('1' * j)
            for k in range(1, mx):
                sk = int('1' * k)
                a.add(si + sj + sk)
    a = list(a)
    a.sort()

    print(a[n - 1])


if __name__ == "__main__":
    main()
