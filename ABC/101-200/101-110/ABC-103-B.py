# ABC-103 B - String Rotation
# https://atcoder.jp/contests/abc103/tasks/abc103_b
#
def getString():
    return input()


def main():
    s = getString()
    t = getString()

    r = 'No'
    for i in range(0, len(s)):
        if t == (s[i:] + s[:i]):
            r = 'Yes'
            break
    print(r)


if __name__ == "__main__":
    main()
