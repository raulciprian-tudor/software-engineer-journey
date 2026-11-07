def main():
    name = input("What's your name? ")

    # if name == 'Harry' or name == 'Hermione' or name == 'Ron':
    #     print('Gryffindor')
    # elif name == 'Draco':
    #     print('Slytherin')
    # else:
    #     print('Who?')

    # We can simplify the code above:
    match name:
        case 'Harry' | 'Hermione' | 'Ron':  # the | character is used to say "or"
            print('Gryffindor')
        case 'Draco':
            print('Slytherin')
        case _:
            print('Who?')


main()
