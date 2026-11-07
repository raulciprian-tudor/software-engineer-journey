def main():
    print(playback())


def playback():
    prompt = input('Say something: ')
    return prompt.replace(' ', '...')


main()
