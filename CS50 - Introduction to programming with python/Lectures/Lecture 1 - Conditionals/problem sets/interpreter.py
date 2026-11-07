prompt = input('Interpret: ')
x = float(prompt.split()[0])
y = prompt.split()[1]
z = float(prompt.split()[2])

match y:
    case '+':
        print(x + z)
    case '-':
        print(x - z)
    case '/':
        print(x / z)
    case '*':
        print(x * z)
