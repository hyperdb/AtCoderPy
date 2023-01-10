# ABC-082 B - Two Anagrams
# https://atcoder.jp/contests/abc082/tasks/abc082_b
#
def getString():
    return input()


def main():
    s = list(getString())
    t = list(getString())

    s.sort()
    t.sort()
    t.reverse()

    print('Yes' if s < t else 'No')


if __name__ == "__main__":
    main()
