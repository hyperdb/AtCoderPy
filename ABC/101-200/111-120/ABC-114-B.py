# ABC-114 B - 754
# https://atcoder.jp/contests/abc114/tasks/abc114_b
#
def getString():
    return input()


def main():
    s = getString()

    t = []
    for i in range(len(s) - 2):
        t.append(abs(int(s[i:i+3]) - 753))
    t.sort()
    print(t[0])


if __name__ == "__main__":
    main()
