def leap_yearp7p2():
    """Ask user to input string value
Once user has input value (year_the_user_has_entered)
Use algo from Lecture8 to verify it is a leap year
The algo works by checking if the year is >=0
and if, year mod 4 == 0 and year mod 100 != 0
or if year mod 400 == 0
mod is short hand for modulo
this returns the signed remainder of  division
then exit program """
help(leap_yearp7p2)

year_the_user_entered = int(input('Plase type a year to check if it is a leap year: '))
print('You have chosen: ', year_the_user_entered)
if (year_the_user_entered % 4 == 0 and year_the_user_entered % 100 != 0) or year_the_user_entered % 400 == 0:
        print(year_the_user_entered, 'is a leap year.')
elif year_the_user_entered >=0:
    print('Your value must be greater than 0')
else:
    print(year_the_user_entered, 'is not a leap year.')
input('Press any key to exit... ' )
#I used a longer variable name instead of year as I wanted to conceptualize it for myself better
