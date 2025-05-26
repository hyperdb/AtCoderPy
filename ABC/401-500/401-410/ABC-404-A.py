# ABC-404 A - Not Found
# https://atcoder.jp/contests/abc404/tasks/abc404_a
#
def getString():
    return input()


def main():
    S = getString()

    for i in range(26):
        c = ord("a") + i
        if chr(c) in S:
            continue
        else:
            print(chr(c))
            break


if __name__ == "__main__":
    main()
