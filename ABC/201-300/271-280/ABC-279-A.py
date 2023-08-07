# ABC-279 A - wwwvvvvvv
# https://atcoder.jp/contests/abc279/tasks/abc279_a
#
def getString():
    return input()


def main():
    s = list(getString())

    print(s.count('v') + s.count('w') * 2)


if __name__ == "__main__":
    main()
