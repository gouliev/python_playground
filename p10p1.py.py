def psuedocode():
    """
Lecture Slides 12 - Exhaustive Enumeration
Loosely referenced our program in slides
CREATE an input float variable
Set epsilon (estimator) and set step 
CREATE a condition if negative integer is input (if/elif)
Assign equation to calculate square root
Print output
"""
help(psuedocode)

epsilon = (0.01)

step = (epsilon ** 2)

input_num = float(input('Enter a positive number to calculate the square root of it: '))
root = 0.0

while abs(input_num - root ** 2) >= epsilon and root ** 2 <= input_num:
    root += step
if abs(input_num - root ** 2) < epsilon:
    print('The square root of', input_num, 'is', root)
elif abs(input_num - root ** 2) > epsilon:
    print('ERROR! Could not find a square root of', input_num)
print('Finished!')
input('Press any key to exit')
