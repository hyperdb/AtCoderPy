# ABC-267 A - Saturday
# https://atcoder.jp/contests/abc267/tasks/abc267_a
#
def getString():
    return input()


def main():
    s = getString()
    d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    print(5 - d.index(s))


if __name__ == "__main__":
    main()
