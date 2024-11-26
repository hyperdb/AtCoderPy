# ABC-380 B - Hurdle Parsing
# https://atcoder.jp/contests/abc380/tasks/abc380_b
#
def getString():
    return input()


def main():
    S = getString()

    sa = S.split("|")

    a = [len(s) for s in sa if s != ""]

    print(" ".join(map(str, a)))


if __name__ == "__main__":
    main()
