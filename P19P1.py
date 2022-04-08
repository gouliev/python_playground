def base_ten(n1, n2): #define function
    """
    Function that takes a number in base 10 and converts to positive integer
    This uses the formula given in class for quotient and divisor
    Condition if int less than 0 entered
    """
    quotient = n1//n2 #set quotient
    remainder_value = n1 % n2 #divisor
    if n1 < n2:
        return ('Error! Please enter positive integer') #condition if 0
    else:
        return quotient + remainder_value

while True:
    base_num = int(input('Please enter the base 10 number: '))
    conversion = int(input('Please enter the required converted number: '))
    print('The result is: ', base_ten(base_num, conversion))