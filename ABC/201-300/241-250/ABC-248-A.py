# ABC-248 A - Lacked Number
# https://atcoder.jp/contests/abc248/tasks/abc248_a
#
def getString():
    return input()


def main():
    a = list(map(int, list(getString())))

    print(45 - sum(a))


if __name__ == "__main__":
    main()
