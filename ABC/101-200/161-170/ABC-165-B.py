# ABC-165 B - 1%
# https://atcoder.jp/contests/abc165/tasks/abc165_b
#
def getInt():
    return int(input())


def main():
    x = getInt()

    a = 100
    c = 0
    while a < x:
        a += a // 100
        c += 1
    print(c)


if __name__ == "__main__":
    main()
