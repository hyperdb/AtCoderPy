# ABC-144 B - 81
# https://atcoder.jp/contests/abc144/tasks/abc144_b
#
def getInt():
    return int(input())


def main():
    n = getInt()

    f = False
    if n < 10:
        f = True
    else:
        for i in range(2, n // 2):
            if i >= 10:
                break
            if n % i == 0 and n // i < 10:
                f = True
                break
    print('Yes' if f else 'No')


if __name__ == "__main__":
    main()
