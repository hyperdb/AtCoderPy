# ABC-402 A - CBC
# https://atcoder.jp/contests/abc402/tasks/abc402_a
#
def getString():
    return input()


def main():
    S = getString()
    T = [c for c in S if ord("A") <= ord(c) <= ord("Z")]

    print("".join(T))


if __name__ == "__main__":
    main()
