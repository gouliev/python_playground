def fibonacci_of(x):
    """
    INPUT integer (NON NEGATIVE)
    FIBONACCI calculation
    IF X is negative. Print ERROR.
    ELSE, call function(x)
    THIS IS A RECURSIVE METHOD
    Function works by returning fib x - 1 + fib of x - 2
    FOR statement to call function 
    PRINT output
    """
    if x <= 1:
        return x
    else:
        return(fibonacci_of(x - 1) + fibonacci_of(x - 2))
help(fibonacci_of)


count = 0
num = int(input('Please enter a number that is a non-negative integer (>=0):   '))
if num < 0:
    print('This number is NOT a non negative integer. Please try this again!')
elif num == 0:
    print('This number is NOT a non negative integer. Please try this again!')
else:
    for i in range(num):
        print (fibonacci_of(i))
        count += 1
print()
print('The number of numbers in the series', num, 'is', count)
('Finished!')
