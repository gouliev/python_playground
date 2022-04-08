def prime():
    """
    Program to illustrate the use of the else statement
    Program set for integers 2, 20 
    Question did not ask us to ask user for input
    Uses FOR statement in another FOR statement
    Checks condition for modulo % 1 == 0:
    """
help(prime)
for num in range(2, 20):
    for i in range(2, num):
        if num % i == 0:
            print(num, 'equals', i, '*', num//i)
            break #breaks the cycle
            
    else:
        # loop fell through without finding a factor
        print(num, 'is a prime number')

print('Finished!')

input('Press any key to exit!')