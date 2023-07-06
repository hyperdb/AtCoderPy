# ABC-260 A - A Unique Letter
# https://atcoder.jp/contests/abc260/tasks/abc260_a
#
def getString():
    return input()


def main():
    s = list(getString())
    l = [s[i] for i in range(3) if s.count(s[i]) == 1]

    print(-1 if len(l) == 0 else l[0])


if __name__ == "__main__":
    main()
