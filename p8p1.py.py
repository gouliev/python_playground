def psuedocode():
    """
Create 3 or 4 INPUTS to create a series of numbers
Use a WHILE loop to check if negative integer
If negative, BREAK
If positive, CONTINUE/PASS #not sure which one
Create if statements/conditions to check Modulos 
If modulos -divisable- is present, i.e. % 2 3 5 7
Print result which of it is divsiable 
Print finished!

"""
help(psuedocode)

num1 = int(input('Please enter 1st num: '))
print('You entered ', num1)
num2 = int(input('Please enter 2nd num: '))
print('You entered ', num2)
num3 = int(input('Please enter 3rd num: '))
print('You entered ', num3)
num4 = int(input('Please enter 4th num: '))
print('You entered ', num4)

while num1 and num2 and num3 and num4 <= 0: 
    print('ERROR! Please enter a positive number!')
    break
    if num1 and num2 and num3 and num4 >= 0:
        pass
if num1 and num2 and num3 and num4 % 2 ==0:
    print('These numbers are divisable by 2')
if num1 and num2 and num3 and num4 % 3 ==0:
    print('These numbers are divisable by 3')
if num1 and num2 and num3 and num4 % 5 ==0:
    print('These numbers are divisable by 5')
if num1 and num2 and num3 and num4 % 7 ==0:
    print('These numbers are divisable by 7')
    
print()
print('Finished!')
input('Press any key to exit!')



