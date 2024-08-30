# ABC-367 B - Cut .0
# https://atcoder.jp/contests/abc367/tasks/abc367_b
#
def getString():
    return input()


def main():
    X = getString()

    print(X.rstrip("0").rstrip("."))


if __name__ == "__main__":
    main()
