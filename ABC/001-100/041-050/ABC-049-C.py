# ABC-049 C - 白昼夢
# https://atcoder.jp/contests/abc049/tasks/arc065_a
#
def getString():
    return input()


def main():
    S = getString()
    keywords = ["dream", "dreamer", "erase", "eraser"]

    while True:
        matched = False
        for kw in keywords:
            if S.endswith(kw):
                S = S[: -len(kw)]
                matched = True
                break
        if not matched:
            break
        if S == "":
            break

    print("YES" if S == "" else "NO")


if __name__ == "__main__":
    main()
