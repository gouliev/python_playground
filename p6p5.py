def my_func():
    """ input(str(.....Hey give me your password?....))
var1 (x, y, z) = stored password
ask user for input....
#f input matches x y z
allow access
else, do not allow
#make 3 seperate inputs (x3)
#when user fails; exits program
"""
help(my_func)


x = 'bike'
y = 'car'
z = 'music'
count = 0
first_try = input(str('What is the password: '))
if first_try == x:
    print('You have successfully logged in.')
elif first_try == y:
    print('You have successfully logged in.')
elif first_try == z:
    print('You have successfully logged in.')
else:
    print('Sorry, the password is wrong.')
count +=1
second_try = input(str('What is the password: '))
if second_try == x:
    print('You have successfully logged in.')
elif second_try == y:
    print('You have successfully logged in.')
elif second_try == z:
    print('You have successfully logged in.')
else:
    print('Sorry, the password is wrong.')
count +=1

final_third_try = input(str('What is the password: '))
if final_third_try == x:
    print('You have successfully logged in.')
elif final_third_try == y:
    print('You have successfully logged in.')
elif final_third_try == z:
    print('You have successfully logged in.')
else:
    print('Sorry, the password is wrong.')
count +=1
if count >= 3:
    print('You have been denied access.')
print()
input('Press any key to continue')
