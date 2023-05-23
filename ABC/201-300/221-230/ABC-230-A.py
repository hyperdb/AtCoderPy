# ABC-230 A - AtCoder Quiz 3
# https://atcoder.jp/contests/abc230/tasks/abc230_a
#
def getInt():
    return int(input())


def main():
    n = getInt()

    print("AGC%03d" % (n if n < 42 else n + 1))


if __name__ == "__main__":
    main()
