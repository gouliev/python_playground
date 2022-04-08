def max_of_func(a, b): #I changed the name of variable to my own choice (i.e. not max, but max_of_func)
    """
    This function finds the largest of two numbers inputted
    It works by comparing A to B
    Then returning A or B depending on size
    The difference between the first P13P1 is:
    This function calls invokes the max in a print statement
    """
    if a > b:
        return a
    else: 
        return b
help(max_of_func)

num1 = float(input('Enter a number please: ')) #Number input
num2 = float(input('Enter a number please: ')) #Second number input

print('The largest of', num1, 'and', num2, 'is', max_of_func(num1, num2)) #Output result
input('Finished! Press any key to exit!')
