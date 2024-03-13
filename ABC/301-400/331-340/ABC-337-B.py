# ABC-337 B - Extended ABC
# https://atcoder.jp/contests/abc337/tasks/abc337_b
#
def getString():
    return input()


def main():
    s = getString()

    old_c = 'A'
    r = True
    for c in s:
        if c >= old_c:
            old_c = c
        else:
            r = False
            break

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
