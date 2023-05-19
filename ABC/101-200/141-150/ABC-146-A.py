# ABC-146 A - Can't Wait for Holiday
# https://atcoder.jp/contests/abc146/tasks/abc146_a
#
def getString():
    return input()


def main():
    s = getString()

    p = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'].index(s)

    print(7 - p)


if __name__ == "__main__":
    main()
