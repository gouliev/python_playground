def print_max(): #First function
    """Program PRINTS out largest of 2 numbers. 2 functions PRINT MAX and MAX. This demonstrates functions within functions"""
    def max(a, b): #Second function in the function
        """This function returns the largest of 2 arguments"""
        if a > b:
            return a 
        else:
            return b
help(print_max)

num1 = float(input('Enter a number please : ')) #Number input
num2 = float(input('Enter a number please: ')) #Second number input
print('The largest of', num1, 'and', num2, 'is', max(num1, num2))

input('Finished! Press any key to exit!')