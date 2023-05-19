# ABC-131 A - Security
# https://atcoder.jp/contests/abc131/tasks/abc131_a
#
def getString():
    return input()


def main():
    s = list(getString())

    f = True
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            f = False
            break
    print('Good' if f else 'Bad')


if __name__ == "__main__":
    main()
