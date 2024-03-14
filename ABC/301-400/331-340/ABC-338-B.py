# ABC-338 B - Frequency
# https://atcoder.jp/contests/abc338/tasks/abc338_b
#
def getString():
    return input()


def main():
    s = getString()
    d = {}
    max_v = 0
    for c in s:
        d.setdefault(c, 0)
        d[c] += 1
        max_v = max(max_v, d[c])

    filter_d = dict(filter(lambda item: item[1] == max_v, d.items()))

    print(sorted(filter_d.keys())[0])


if __name__ == "__main__":
    main()
