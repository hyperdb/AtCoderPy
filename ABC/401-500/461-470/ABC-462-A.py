# ABC-462 A - Secret Numbers
# https://atcoder.jp/contests/abc462/tasks/abc462_a
#
def getString():
    return input()


def main():
    S = getString()
    T = []

    for s in S:
        if "0" <= s <= "9":
            T.append(s)
    print("".join(T))


if __name__ == "__main__":
    main()
