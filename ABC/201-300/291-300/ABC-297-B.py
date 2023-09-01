# ABC-297 B - chess960
# https://atcoder.jp/contests/abc297/tasks/abc297_b
#
def getString():
    return input()


def main():
    s = getString()

    r = False
    if s.find('B') % 2 != s.rfind('B') % 2 and s.find('R') < s.find('K') < s.rfind('R'):
        r = True

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
