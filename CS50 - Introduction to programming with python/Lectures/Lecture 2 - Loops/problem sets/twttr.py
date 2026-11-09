import re


def main():
    prompt = input('Input: ')
    filtered_input = filter_vowels(prompt)
    print(filtered_input)


def filter_vowels(input):
    return re.sub(r'[AEIOUaeiou]', '', input)


main()
