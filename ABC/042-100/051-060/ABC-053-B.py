# ABC-053 B - A to Z String
# https://atcoder.jp/contests/abc053/tasks/abc053_b
#
def getString():
    return input()


def main():
    s = getString()

    print(s.rfind('Z') - s.find('A') + 1)


if __name__ == "__main__":
    main()
