def psuedocode():
    """
    CREATE input
    Create TRUE statement
    CONDITION if neg int entered
    BREAK if so, CONTINUE if not
    USE conditional statements to create factorial
    USE for i in range 
    FACTORIAL is *= i
    Print output
    Finish!
    """
help(psuedocode)



while True:
    num = int(input('Enter a positive int: '))
    if num <0:
        print('ERROR! Negative integer!')
        break
    else:
        if num == 0:
            fact = 1
        elif num == 1:
            fact = 1
        else:
            fact = 1
            for i in range(1, num + 1):
                fact *= i
        print('Factorial of', num, 'is', fact)
