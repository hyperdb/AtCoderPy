# ABC-235 A - Rotate
# https://atcoder.jp/contests/abc235/tasks/abc235_a
#
def getString():
    return input()


def main():
    abc = list(map(int, list(getString())))

    print(111 * sum(abc))

if __name__ == "__main__":
    main()