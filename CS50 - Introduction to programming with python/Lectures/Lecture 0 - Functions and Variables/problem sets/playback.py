def main():
    # ask user for his though
    words = input("What's on your mind? ")
    print(slow_down(words))


def slow_down(words):
    # split the words
    list_words = words.split()
    # join the split words with a separator
    return '...'.join(list_words)


main()
