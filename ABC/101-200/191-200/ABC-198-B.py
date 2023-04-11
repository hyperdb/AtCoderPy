# ABC-198 B - Palindrome with leading zeros
# https://atcoder.jp/contests/abc198/tasks/abc198_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    m = str(int(str(n)[::-1]))

    print('Yes' if m == m[::-1] else 'No')


if __name__ == "__main__":
    main()
