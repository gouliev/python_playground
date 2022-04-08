def recursive(n):  #named function
    """
        2 BASE CASES
        If N=1, return 2
        If N>1, return 2xf(n-1)
        Create INPUT
        Create condition if n<1 within function
        Invoke function call when user inputs int
        Print statements to show progress
        Similar assignment to P12-P15 where we define recursive function
    """
    if n == 1:
        return 2
    elif n < 1: #if neg int entered
        print('Error!')
    else:
        print('The series of', n)
        return 2 * recursive(n - 1) #equation given in piecewise function (recrusive series)

help(recursive)

while True:
    num = int(input('Please enter a num: ')) #input
    print('Finding the term of', num, 'in the following recursive series')
    if num < 0:
        print('Sorry, your input results in: ', recursive(0))
    elif num ==1:
        print('The result is', recursive(1))
    else:
        print('The result is', recursive(num), 'for input', num) #function invoked
