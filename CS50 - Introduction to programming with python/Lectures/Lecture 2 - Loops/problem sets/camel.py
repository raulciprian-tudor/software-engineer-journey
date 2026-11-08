import re


def main():
    prompt = input('camelCase? ')
    snakeCase(prompt)


def snakeCase(camel_case):
    words = re.findall('([A-Za-z][a-z]*)', camel_case)
    lower_words = []

    for word in words:
        lower_words.append(word.lower())

    print(f'snake_case: {"_".join(lower_words)}')


main()
