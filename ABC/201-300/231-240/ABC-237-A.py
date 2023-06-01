# ABC-237 A - Not Overflow
# https://atcoder.jp/contests/abc237/tasks/abc237_a
#
def getInt():
    return int(input())

def main():
    n = getInt()

    print('Yes' if -2 ** 31 <= n < 2 ** 31 else 'No')


if __name__ == "__main__":
    main()