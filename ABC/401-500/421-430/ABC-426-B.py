# ABC-426 B - The Odd One Out
# https://atcoder.jp/contests/abc426/tasks/abc426_b
#
def getString():
    return input()


def main():
    S = list(getString())

    for c in set(S):
        if S.count(c) > 1:
            continue
        print(c)


if __name__ == "__main__":
    main()
