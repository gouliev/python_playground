def fibonacci(n):#Function for the n'th fibonacci number
    """
    CHECK IF INPUT IS LESS THAN 0
    Print ERROR if it is
    CHECK if N = 0
    Return 0
    Check if N = 1 or 2
    Return 1 if it is
    ELSE statement calculate fibonnaci
    CREATE input LOOP
    "i.e., prompt a series", ask multiple times..
    Implement invoke function to call it
    """
    if n < 0:
        print('ERROR! Please input non negative integer!')
    elif n == 0:
        print('The base case of n = 0 has been reached')
        return 0
    elif n == 1:
        print('The base case of n = 1 has been reached')
        return 1
    else:
        print('The base case has NOT been reached for n=' + str(n) + '! Trying again!')
        return(fibonacci(n-1) + fibonacci(n-2))

help(fibonacci)

while True:
    num = int(input('Please enter a number to print out its Fibonacci series: '))
    print('The fibonacci of', num, 'is', fibonacci(num))
    print()

print('Finished!')
