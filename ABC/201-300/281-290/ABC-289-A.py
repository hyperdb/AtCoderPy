# ABC-289 A - flip
# https://atcoder.jp/contests/abc289/tasks/abc289_a
#
def getString():
    return input()


def main():
    s = getString()

    t = [i ^ 1 for i in list(map(int, list(s)))]

    print("".join(list(map(str, t))))


if __name__ == "__main__":
    main()
