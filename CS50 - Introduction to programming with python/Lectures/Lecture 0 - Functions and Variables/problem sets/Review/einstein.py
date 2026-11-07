def main():
    print(einstein())


def einstein():
    m = int(input("What's m? "))
    c = 300000000
    e = m * pow(c, 2)

    return f'{e:,}'


main()
