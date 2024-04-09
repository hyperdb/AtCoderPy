# ABC-347 B - Substring
# https://atcoder.jp/contests/abc347/tasks/abc347_b
#
def getString():
    return input()


def main():
    s = getString()

    t = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            t.append(s[i:j+1])

    print(len(set(t)))


if __name__ == "__main__":
    main()
