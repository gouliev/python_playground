def my_func():
    """
create an input(str( to ask for PW from user
create a counter with limit of 3
this will keep track of number of tries
create if statement if PW successful
create another statement to deny access after 3 attempts """
help(my_func)

password = 'COMP10280'
count = 0
attempt1 = input('Please enter your password: ')
if attempt1 != password:
    print('Sorry, the password is wrong.')
elif attempt1 == password:
    print('You have successfully logged in.')
count +=1
attempt2 = input('Please enter your password: ')
if attempt2 != password:
    print('Sorry, the password is wrong.')
elif attempt2 == password:
    print('You have successfully logged in')
count +=1
attempt3 = input('Please enter your password: ')
if attempt3 != password:
    print('Sorry, the password is wrong')
elif attempt3 == password:
    print('You have successfully logged in')
count +=1
if count >= 3:
    print('You have been denied access.')
