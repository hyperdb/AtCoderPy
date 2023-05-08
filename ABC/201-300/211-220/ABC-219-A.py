# ABC-219 A - AtCoder Quiz 2
# https://atcoder.jp/contests/abc219/tasks/abc219_a
#
def getInt():
    return int(input())


def main():
    x = getInt()

    print('expert' if x >= 90 else 90 - x if x >=
          70 else 70 - x if x >= 40 else 40 - x)


if __name__ == "__main__":
    main()
