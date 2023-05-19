# ABC-225 A - Distinct Strings
# https://atcoder.jp/contests/abc225/tasks/abc225_a
#
import itertools


def getString():
    return input()


def main():
    s = list(getString())
    t = ["".join(w) for w in itertools.permutations(s, 3)]

    print(len(set(t)))


if __name__ == "__main__":
    main()
