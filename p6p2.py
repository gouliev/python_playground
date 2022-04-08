def my_func():
    """
create 3 inputs from user
input(str(..))
use if and else conditions to find modulo 2 for odd num
find largest number using max function max(total)
else statement if no odd number
print result if large int present
    """
help(my_func)

a = int(input('Enter your first integer: '))
b = int(input('Enter your second integer: '))
c = int(input('Enter your third integer: '))

if a%2 ==0:
    a = 0  
else:
    a = a 
if b%2 ==0:
    b = 0 
else:
    b = b
if c%2 ==0:
    c = 0
else:
    c = c 

total= a, b, c

max = max(total)
if max ==0:
    print('There are no odd numbers.')
else: 
    print (max, 'is the largest odd number.')
