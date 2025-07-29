# ABC-415 B - Pick Two
# https://atcoder.jp/contests/abc415/tasks/abc415_b
#
def getString():
    return input()


def main():
    S = getString()

    T = [i + 1 for i in range(len(S)) if S[i] == "#"]

    for x in range(0, len(T), 2):
        print("{},{}".format(T[x], T[x + 1]))


if __name__ == "__main__":
    main()
