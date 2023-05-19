# ABC-122 A - Double Helix
# https://atcoder.jp/contests/abc122/tasks/abc122_a
#
def getString():
    return input()


def main():
    b = getString()
    l = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    print(l[b])


if __name__ == "__main__":
    main()
