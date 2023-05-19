# ABC-206 A - Maxi-Buying
# https://atcoder.jp/contests/abc206/tasks/abc206_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    p = (n * 1.08) // 1

    print('Yay!' if p < 206 else ':(' if p > 206 else 'so-so')


if __name__ == "__main__":
    main()
