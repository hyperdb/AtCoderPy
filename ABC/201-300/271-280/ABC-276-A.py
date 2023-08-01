# ABC-276 A - Rightmost
# https://atcoder.jp/contests/abc276/tasks/abc276_a
#
def getString():
    return input()


def main():
    s = list(getString())

    s.reverse()

    print(len(s) - s.index('a') if 'a' in s else -1)


if __name__ == "__main__":
    main()
