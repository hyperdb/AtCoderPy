# ABC-324 B - 3-smooth Numbers
# https://atcoder.jp/contests/abc324/tasks/abc324_b
#
def getInt():
    return int(input())


def div(n, x):
    while n % x == 0:
        n //= x
    return n


def main():
    n = getInt()

    print('Yes' if div(div(n, 2), 3) == 1 else 'No')


if __name__ == "__main__":
    main()
