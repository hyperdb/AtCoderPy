# ABC-033 A - 暗証番号
# https://atcoder.jp/contests/abc033/tasks/abc033_a
#
def getString():
    return input()


def main():
    N = set(list(getString()))

    print("SAME" if len(N) == 1 else "DIFFERENT")


if __name__ == "__main__":
    main()
