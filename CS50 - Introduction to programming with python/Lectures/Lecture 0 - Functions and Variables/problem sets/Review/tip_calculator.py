def main():
    dollars = dollars_to_float(input('How much was the meal? '))
    percent = percent_to_float(input('What percentage would you like to tip? '))
    tip = dollars * percent
    print(f'Leave ${tip:.2f}')


def dollars_to_float(d):
    format_d = d.replace('$', '')
    return float(format_d)


def percent_to_float(p):
    format_p = p.replace('%', '')
    return float(format_p) / 100


main()
