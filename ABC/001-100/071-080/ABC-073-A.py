# ABC-073 A - September 9
# https://atcoder.jp/contests/abc073/tasks/abc073_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print('Yes' if n // 10 == 9 or n % 10 == 9 else 'No')


if __name__ == "__main__":
    main()
