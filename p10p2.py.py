def psuedocode():
    """
Create TRUE condition so it loops and asks a series of times
Create INPUT
COUNTER for cube_root (augment assignment +=)
IF conditions for negative cube root
Output the result of cube root ** 3
FINISH
"""
help(psuedocode)





cube_root = 0
while True:
    num = int(input('Enter a number to find the integer cube root of the number please: '))
    while cube_root ** 3 < abs(num):
        cube_root = cube_root + 1
    if cube_root ** 3 == abs(num):
        if num <0:
            cube_root = -cube_root
        print('The cube root of', num, 'is', cube_root)
    else:
        print('The number is not a perfect cube!')
    
print('Finished')
input('Press any key to exit')
