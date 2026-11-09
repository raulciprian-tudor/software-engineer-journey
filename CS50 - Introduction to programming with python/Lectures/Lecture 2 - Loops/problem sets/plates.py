import re


def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s) -> bool:
    return re.fullmatch(r'(?=.{2,6}$)[A-Za-z]{2,}([1-9][0-9]*)?', s) is not None


main()
