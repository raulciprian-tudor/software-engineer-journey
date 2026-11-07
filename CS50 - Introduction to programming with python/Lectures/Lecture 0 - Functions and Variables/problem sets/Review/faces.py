def main():
    faces()


def faces():
    prompt = input('Say something: ')
    prompt = prompt.replace(':)', '🙂')
    prompt = prompt.replace(':(', '🙁')

    print(prompt)


main()
