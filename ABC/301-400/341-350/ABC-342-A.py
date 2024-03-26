# ABC-342 A - Yay!
# https://atcoder.jp/contests/abc342/tasks/abc342_a
#
def getString():
    return input()


def main():
    s = list(getString())

    for c in set(s):
        if s.count(c) == 1:
            print(s.index(c) + 1)
            break


if __name__ == "__main__":
    main()
