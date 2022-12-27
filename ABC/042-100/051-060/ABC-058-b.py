# ABC-058 B - ∵∴∵
# https://atcoder.jp/contests/abc058/tasks/abc058_b
#
def getString():
    return input()


def main():
    o = getString()
    e = getString()

    r = len(o) if len(o) <= len(e) else len(e)

    s = ''
    for i in range(r):
        s = s + o[i] + e[i]
    if len(o) > r:
        s = s + o[-1 * (len(o) - r)]
    elif len(e) > r:
        s = s + e[-1 * (len(e) - r)]
    print(s)


if __name__ == "__main__":
    main()
