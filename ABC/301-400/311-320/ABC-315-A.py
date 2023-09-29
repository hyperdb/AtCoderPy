# ABC-315 A - tcdr
# https://atcoder.jp/contests/abc315/tasks/abc315_a
#
def getString():
    return input()

def main():
    s = list(getString())
    t = [c for c in s if c not in ['a', 'e', 'i', 'o', 'u']]

    print("".join(t))


if __name__ == "__main__":
    main()