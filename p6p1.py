def my_func():"""
    
prompt user for int first number
prompt user for int second number
sum the total number
create if statement to determine int size
print result if int larger than 100 """
    
help(my_func)

print()
print()
print()

number1 = int(input('Please enter your first number: '))
number2 = int(input('Please enter your second number: '))
total = number1 + number2
if total > 100:
    print('That is a big number!')

input('Press any key to exit ...')
