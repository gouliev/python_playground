def find_divisor_of(n1, n2):
    """
    This function finds the common divisors of 2 numbers
    The numbers are assumed to be positive integers
    This returns a tuple containing the common divisors
    This program demonstrates the use of tuples
    This program was loosely taken from Lecture 16
    From the permission of John as per question
    Creating a for condition using modulo % 1 and % 2 to find remainder
    Then creating return
    Creating inputs and calling the function
    Then creating a sum to print the total
    Assignment did not ask to print sum
    However I included this for my own benefit of understanding it"""

    divisors = ()
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0: #remainder, doing the arithmetic using modulo operation
            divisors += (i,)
    return divisors

help(find_divisor_of)

while True:
    num1 = int(input('Enter a positive integer: '))
    num2 = int(input('Enter another a positive integer: '))

    if num1 <= 0 or num2 <= 0:
        print('Numbers should be less than or equal 0')
    else: #Here we are getting the common divisors and printing them all out
        divisors = find_divisor_of(num1, num2)
        print('The common divisors of', num1, 'and', num2, 'are:', divisors)
        total = 0
        for d in divisors: #summing them and printing out the total
            total += d
        print('The sum of the common divisors is:', total) #prints sum