# ABC-218 A - Weather Forecast
# https://atcoder.jp/contests/abc218/tasks/abc218_a
#
def getInt():
    return int(input())


def getString():
    return input()


def main():
    n = getInt()
    s = list(getString())

    print('Yes' if s[n - 1] == 'o' else 'No')


if __name__ == "__main__":
    main()
