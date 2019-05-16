def without_repetition(t):
    s = set()
    o = []
    for c in t:
        if c not in s:
            s.add(c)
            o.append(c)
    return ''.join(o)


def main():
    s = input()
    k = int(input())
    n = len(s)
    w = k
    for t in [s[i:i + w] for i in range(0, n, w)]:
        print(without_repetition(t))


main()
