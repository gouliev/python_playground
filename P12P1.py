def square_root(x):
    """
    INPUT x 2
    INT for limit (tolerance)
    Calculate SQUARE_ROOT within FUNCTION
    Invoke function with FOR statement
    I had some issue with this one so caveat!
    """
    epsilon = 0.01
    step = epsilon ** 2
    root = 0.0
    while abs(x - root ** 2) >= epsilon and root ** 2 <= x:
        root += step
    if abs(x - root ** 2) < epsilon:
        print('The approximate square root of', x, 'is', root)
    else:
        print('Failed to find a square root of', x)

help(square_root)
num = int(input('Enter the num for which you wish to calculate the square root: '))
tolerance = int(input('Enter a tolerance: '))

for i in range(num, tolerance):
    print('The square root is,', (square_root(i)))
