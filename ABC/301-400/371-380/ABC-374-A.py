# ABC-374 A - Takahashi san 2
# https://atcoder.jp/contests/abc374/tasks/abc374_a
#
def getString():
    return input()


def main():
    S = getString()

    print("Yes" if S[-3:] == "san" else "No")


if __name__ == "__main__":
    main()
