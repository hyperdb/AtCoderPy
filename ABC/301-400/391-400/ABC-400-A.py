# ABC-400 A - ABC400 Party
# https://atcoder.jp/contests/abc400/tasks/abc400_a
#
def getInt():
    return int(input())


def main():
    A = getInt()

    d, m = divmod(400, A)

    print(d if m == 0 else -1)


if __name__ == "__main__":
    main()
