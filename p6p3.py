def my_func():
	"""
ask user for name using input(str(..)
before doing that, create your name and store as var
create 2 other vars to store 'Mickey..' and 'Spongebob..'
create if and else conditions to print message
	"""
help(my_func)

var1 = 'Zaur'
var2 = 'Mickey Mouse'
var3 = 'Spongebob Squarepants'
name = input(str('What is your name? '))
if name == var1:
    print('That is a cool name!')
elif name == var2:
    print('I am not sure that is your name')
elif name == var3:
    print('I am not sure that is your name')
else:
    print('That is also a cool name, but my name is cooler!')

input('Press any key to continue ...')
