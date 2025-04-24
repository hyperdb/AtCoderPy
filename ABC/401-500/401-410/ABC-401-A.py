# ABC-401 A - Status Code
# https://atcoder.jp/contests/abc401/tasks/abc401_a
#


def getString():
    return input()


def main():
    S = getString()

    print("Success" if 200 <= int(S) <= 299 else "Failure")


if __name__ == "__main__":
    main()
