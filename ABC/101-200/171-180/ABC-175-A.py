# ABC-175 A - Rainy Season
# https://atcoder.jp/contests/abc175/tasks/abc175_a
#
def getString():
    return input()


def main():
    s = getString()

    c = 0
    for i in [3, 2, 1]:
        if 'R' * i in s:
            c = i
            break
    print(c)


if __name__ == "__main__":
    main()
