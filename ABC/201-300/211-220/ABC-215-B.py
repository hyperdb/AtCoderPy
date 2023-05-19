# ABC-215 B - log2(N)
# https://atcoder.jp/contests/abc215/tasks/abc215_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    i = 0
    while 2 ** (i + 1) <= n:
        i += 1
    print(i)


if __name__ == "__main__":
    main()
