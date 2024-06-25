# ABC-357 B - Uppercase and Lowercase
# https://atcoder.jp/contests/abc357/tasks/abc357_b
#
def getString():
    return input()


def main():
    S = getString()

    up = 0
    low = 0
    for x in list(S):
        if "a" <= x <= "z":
            low += 1
        else:
            up += 1

    print(S.upper() if up > low else S.lower())


if __name__ == "__main__":
    main()
