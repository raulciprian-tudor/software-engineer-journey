def main():
    x = int(input("What's x? "))

    if is_even(x):
        print('even')
    else:
        print('odd')


def is_even(n):
    # if n % 2 == 0:
    #     return True

    return n % 2 == 0  # boolean expression returns either True or False


main()
