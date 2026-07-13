# ABC-464 A - Decisive Battle
# https://atcoder.jp/contests/abc464/tasks/abc464_a
#
def getString():
    return input()


def main():
    S = getString()

    print("East" if S.count("E") > S.count("W") else "West")


if __name__ == "__main__":
    main()
