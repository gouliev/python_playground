original_amount = float(input('Please enter your amount: '))
rate_usd = 1.17
conversion = (original_amount * rate_usd)


if original_amount >= 0:
    print('Your converted amount is ', conversion)
elif original_amount < 0:
    print('Amount must be greater than or equal to 0. Please try again')

input("Press any key to continue...  ")
