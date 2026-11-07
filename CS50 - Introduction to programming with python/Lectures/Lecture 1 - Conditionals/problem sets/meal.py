def main():
    time = input('What is the time? ')
    convert(time)


def convert(time):
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])

    if hour == 7 and 0 <= minute < 60:
        print('breakfast time')
    elif hour == 12 and 0 <= minute < 60:
        print('lunch time')
    elif hour == 18 and 0 <= minute < 60:
        print('dinner time')


if __name__ == '__main__':
    main()
