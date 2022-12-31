# ABC-069 B - i18n
# https://atcoder.jp/contests/abc069/tasks/abc069_b
#
def getString():
    return input()


def main():
    s = getString()

    print(s[0] + str(len(s) - 2) + s[-1])


if __name__ == "__main__":
    main()
