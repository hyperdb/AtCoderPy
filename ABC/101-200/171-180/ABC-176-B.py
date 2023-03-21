# ABC-176 B - Multiple of 9
# https://atcoder.jp/contests/abc176/tasks/abc176_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    l = map(int, list(str(n)))

    print('Yes' if sum(l) % 9 == 0 else 'No')


if __name__ == "__main__":
    main()
