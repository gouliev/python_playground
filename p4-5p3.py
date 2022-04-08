income = float(input('Please input your gross income: '))
lower_income = (income*0.6)
higher_income = (income*0.4)
lower_tax = (lower_income*0.41)
higher_tax = (higher_income*0.23)
total_tax = (lower_tax + higher_tax)
net_income = (income - total_tax)

"""The upper band given
is taxed at 23%
and lower band is 41%"""

print()

if income <=0:
    print('Amount of income must be >= 0. Please try again.')
else:
    print('Your gross amount is',income,', the first (low tax band) is', lower_tax,
      'the second (higher tax band) is', higher_tax,'. The total tax due is',
      total_tax, 'and the total net income (initial amount less taxes) is',
      net_income)

input('Press any key to continue... ' )
