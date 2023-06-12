# ABC-242 B - Minimize Ordering
# https://atcoder.jp/contests/abc242/tasks/abc242_b
#
def getString():
    return input()

def main():
    s = list(getString())

    s.sort()

    print("".join(s))

if __name__ == "__main__":
    main()