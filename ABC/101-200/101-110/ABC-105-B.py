# ABC-105 B - Cakes and Donuts
# https://atcoder.jp/contests/abc105/tasks/abc105_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    r = 'No'
    for i in range(n // 7 + 1):
        if (n - (7 * i)) % 4 == 0:
            r = 'Yes'
            break
    print(r)


if __name__ == "__main__":
    main()
