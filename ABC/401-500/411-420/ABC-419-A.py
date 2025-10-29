# ABC-419 A - AtCoder Language
# https://atcoder.jp/contests/abc419/tasks/abc419_a
#
def getString():
    return input()


def main():
    S = getString()
    d = {"red": "SSS", "blue": "FFF", "green": "MMM"}

    print(d[S] if S in d else "Unknown")


if __name__ == "__main__":
    main()
