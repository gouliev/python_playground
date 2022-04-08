def factorial(x):
    """Defines the factorial of a given non negative integer"""
    if x == 0:
        print('The base case of n = 0 has been reached')
        return 1
    else:
        print('The base case has NOT been reached for n=' + str(x) + '! Trying again!')
        return x * factorial(x - 1)
help(factorial)

num = int(input('Please enter a num: '))

if num <=0:
     print('ERROR, please input a non negative integer!')
else:
    print('The factorial of', num, 'is', factorial(num))

print('Finished!')
input('Press any key to exit!')