# ABC-345 B - Integer Division Returns
# https://atcoder.jp/contests/abc345/tasks/abc345_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    d, m = divmod(n, 10)

    print(d if m == 0 else d + 1)


if __name__ == "__main__":
    main()
