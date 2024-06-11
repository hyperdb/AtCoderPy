# ABC-078 A - Good Integer
# https://atcoder.jp/contests/abc079/tasks/abc079_a
#
def getString():
    return input()


def main():
    n = list(getString())
    n.sort()

    print('Yes' if n[0] == n[1] and n[0] == n[2] else 'No')


if __name__ == "__main__":
    main()
