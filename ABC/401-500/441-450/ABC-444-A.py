# ABC-444 A - Repdigit
# https://atcoder.jp/contests/abc444/tasks/abc444_a
#
def getString():
    return input()


def main():
    S = list(getString())

    print("Yes" if len(set(S)) == 1 else "No")


if __name__ == "__main__":
    main()
