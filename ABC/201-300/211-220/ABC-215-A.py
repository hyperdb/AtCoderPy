# ABC-215 A - Your First Judge
# https://atcoder.jp/contests/abc215/tasks/abc215_a
#
def getString():
    return input()


def main():
    s = getString()

    print('AC' if s == 'Hello,World!' else 'WA')


if __name__ == "__main__":
    main()
