# ABC-442 A - Count .
# https://atcoder.jp/contests/abc442/tasks/abc442_a
#
def getString():
    return input()


def main():
    S = list(getString())

    print(S.count("i") + S.count("j"))


if __name__ == "__main__":
    main()
