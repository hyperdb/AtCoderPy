# ABC-053 C - X: Yet Another Die Game
# https://atcoder.jp/contests/abc053/tasks/arc068_a
#
def getInt():
    return int(input())


def main():
    N = getInt()

    d, m = divmod(N, 11)  # 6 -> 5 ->
    d *= 2

    if m > 0:
        d += 1 if m <= 6 else 2

    print(d)


if __name__ == "__main__":
    main()
