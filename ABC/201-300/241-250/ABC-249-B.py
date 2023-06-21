# ABC-249 B - Perfect String
# https://atcoder.jp/contests/abc249/tasks/abc249_b
#
def getString():
    return input()


def main():
    s = list(getString())

    lo = [c for c in s if c >= 'a' and c <= 'z']
    up = [c for c in s if c >= 'A' and c <= 'Z']

    if len(lo) == 0 or len(up) == 0:
        print('No')
    elif len(lo) != len(set(lo)):
        print('No')
    elif len(up) != len(set(up)):
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    main()
