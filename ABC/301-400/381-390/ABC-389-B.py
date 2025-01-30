# ABC-389 B - tcaF
# https://atcoder.jp/contests/abc389/tasks/abc389_b
#
def getInt():
    return int(input())


def main():
    X = getInt()

    f = 1
    for i in range(2, X):
        f *= i
        if f == X:
            print(i)
            break


if __name__ == "__main__":
    main()
