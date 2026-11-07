greeting = input('Greeting: ').lower()

if greeting.split(',')[0] == 'hello':
    print('0$')
elif greeting[0] == 'h' and greeting.split(',')[0] != 'hello':
    print('20$')
else:
    print('100$')
