# ABC-445 A - Strong Word
# https://atcoder.jp/contests/abc445/tasks/abc445_a
#
def getString():
    return input()


def main():
    S = getString()

    print("Yes" if S[0] == S[-1] else "No")


if __name__ == "__main__":
    main()
