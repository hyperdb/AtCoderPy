# ABC-043 B - Varied
# https://atcoder.jp/contests/abc063/tasks/abc063_b
#
def getString():
    return input()


def main():
    s = list(getString())
    t = list(set(s))

    print('yes' if len(s) == len(t) else 'no')


if __name__ == "__main__":
    main()
