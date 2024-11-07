# ABC-377 A - Rearranging ABC
# https://atcoder.jp/contests/abc377/tasks/abc377_a
#
def getString():
    return input()


def main():
    S = list(getString())

    S.sort()

    print("Yes" if "".join(S) == "ABC" else "No")


if __name__ == "__main__":
    main()
