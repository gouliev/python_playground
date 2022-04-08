def max_of_func(a, b):  #I changed the name of variable to my own choice (i.e. not max, but max_of_func)
    """
    This function finds the largest of two numbers inputted
    It works by comparing A to B
    Then returning A or B depending on size
    """
    if a > b:
        return a
    else: 
        return b
help(max_of_func)

num1 = float(input('Enter a number please: ')) #Number input
num2 = float(input('Enter a number please: ')) #Second number input

largest = max_of_func(num1, num2) #Invoke function inside named variable 'largest'

print('The largest of', num1, 'and', num2, 'is', largest) #Output result
input('Finished! Press any key to exit!')
