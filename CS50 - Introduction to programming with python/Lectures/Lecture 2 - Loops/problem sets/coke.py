def main():
    total = 50
    while total != 0:
        amount = int(input('Insert coin: '))

        if amount == 5 or amount == 10 or amount == 25:
            total -= amount
            if total >= 0:
                print(f'Amount due: {total}')
                if total == 0:
                    print("Here's your coke!")
            elif total < 0:
                print(f'Change owed: {abs(total)}')
                break
        else:
            print('Please enter 5, 10 or 25 cent coins')


main()
