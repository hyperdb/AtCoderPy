# ABC-080 B - Harshad Number
# https://atcoder.jp/contests/abc080/tasks/abc080_b
#
def getInt():
    return int(input())


def main():
    x = getInt()
    l = map(int, list(str(x)))

    print('Yes' if x % sum(l) == 0 else 'No')


if __name__ == "__main__":
    main()
