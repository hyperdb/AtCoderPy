# ABC-068 B - Break Number
# https://atcoder.jp/contests/abc068/tasks/abc068_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    m = 0
    for i in range((n // 2) + 1):
        if 2 ** i <= n:
            m = 2 ** i

    print(m)


if __name__ == "__main__":
    main()
