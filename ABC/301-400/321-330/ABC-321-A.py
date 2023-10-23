# ABC-321 A - 321-like Checker
# https://atcoder.jp/contests/abc321/tasks/abc321_a
#
def getString():
    return input()


def main():
    n = list(map(int, list(getString())))

    r = True
    if len(n) > 1:
        c = [n[i - 1] - n[i] for i in range(1, len(n))]
        if min(c) <= 0:
            r = False

    print('Yes' if r else 'No')


if __name__ == "__main__":
    main()
