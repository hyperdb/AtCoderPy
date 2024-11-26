# ABC-380 A - 123233
# https://atcoder.jp/contests/abc380/tasks/abc380_a
#
def getString():
    return input()


def main():
    N = list(getString())

    r = True
    for i in [1, 2, 3]:
        if N.count(str(i)) != i:
            r = False
            break
    print("Yes" if r else "No")


if __name__ == "__main__":
    main()
