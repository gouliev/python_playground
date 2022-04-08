def base_ten(n1, n2): #define function
    """
    Function that takes a number in base 10 and converts to positive integer
    This uses the formula given in class for quotient and divisor
    Condition if int less than 0 entered
    Similar to previous question but this one converts to BASE 16 with condition
    """
    quotient = n1//n2 #set quotient
    remainder_value = n1 % n2 #divisor
    if n1 < n2:
        return ('Error! Please enter positive integer') #condition if 0
    if n1 > n2:
        return quotient + remainder_value
    if 'A' in n1 == 10: 
        return base_ten(n1, n2)
    if 'B' in n1 == 11: 
        return base_ten(n1, n2)
    if 'C' in n1 == 12: 
        return base_ten(n1, n2)
    if 'D' in n1 == 13: 
        return base_ten(n1, n2)
    if 'E' in n1 == 14: 
        return base_ten(n1, n2)
    if 'F' in n1 == 15: 
        return base_ten(n1, n2)

while True:
    base_num = int(input('Please enter the base 10 number: '))
    conversion = int(input('Please enter the required converted number: '))
    print('The result is: ', base_ten(base_num, conversion))