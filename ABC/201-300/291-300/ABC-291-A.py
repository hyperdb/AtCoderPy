# ABC-291 A - camel Case
# https://atcoder.jp/contests/abc291/tasks/abc291_a
#
def getString():
    return input()


def main():
    s = list(getString())

    for i in range(len(s)):
        if s[i] <= 'Z':
            print(i + 1)
            break


if __name__ == "__main__":
    main()
