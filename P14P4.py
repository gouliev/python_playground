def prime():
    """
    Program to illustrate the use of the else statement on a for loop
    Search for prime numbers in a range of integers
    The difference here between previous one is this version
    Prints out all the pairs of factors.
    We simply remove the BREAK statement
    I had to think about this for awhile
    I trial and experimented with it, example
    I tried print(i) then realized the BREAK was the only thing stopping it
    I trialed with 2, 40 since it does not ask us to ask user for input
    """
help(prime)
for num in range(2, 40):
    for i in range(2, num):
        if num % i == 0:
            print(num, 'equals', i, '*', num//i)            
    else:
        # loop fell through without finding a factor
        print(num, 'is a prime number')

print('Finished!')

#another step would be there that it prints that every number is a prime number
#consider using some sort of boolean to store when you find a factor
#then you can check before you print that the number is prime

input('Press any key to exit!')