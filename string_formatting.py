def print_formatted(number):
    max_width = len("{0:b}".format(number))

    for i in range(1, number +1):
        decimal = "{0}".format(i).rjust(max_width)
        octal = "{0:o}".format(i).rjust(max_width)
        hexadecimal = "{0:x}".format(i).upper().rjust(max_width)
        binary = "{0:b}".format(i).rjust(max_width)

        print("%s %s %s %s" % (decimal, octal, hexadecimal, binary))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
