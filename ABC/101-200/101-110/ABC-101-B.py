# ABC-101 B - Digit Sums
# https://atcoder.jp/contests/abc101/tasks/abc101_b
#
def getInt():
    return int(input())


def main():
    n = getInt()
    s = sum(map(int, list(str(n))))

    print('Yes' if n % s == 0 else 'No')


if __name__ == "__main__":
    main()
