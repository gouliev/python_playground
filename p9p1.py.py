def psuedocode():
    """
Ask user for INPUT
Create condition if INPUT negative
ELSE continue
Create counter
Use LOOP while statement
Create augmented assignment += and -= to initiate
PRINT output

"""

help(psuedocode)

number = int(input('Enter a positive integer: '))
if number < 0: 
    print('Please only input positive integers!')
else:
    sum = 0
    while number > 0:
        sum += number
        number -=1
    print('The sum of all integers is', sum)
    
print('Finished!')
