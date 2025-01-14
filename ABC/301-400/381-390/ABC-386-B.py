# ABC-386 B - Calculator
# https://atcoder.jp/contests/abc386/tasks/abc386_b
#
def getString():
    return input()


def main():
    S = list(getString())

    buf = ""
    r = 0
    for c in S:
        if c == "0":
            buf += c
        else:
            r += 1
            if buf != "":
                d, m = divmod(len(buf), 2)
                r += d + m
            buf = ""
    # 最後が"0"の場合
    if buf != "":
        d, m = divmod(len(buf), 2)
        r += d + m

    print(r)


if __name__ == "__main__":
    main()
