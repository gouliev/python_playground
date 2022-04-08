def sum5000():
    """
Create a total var and a num var to store initial values
Use while function to set a limit, i.e. <= 5000
Initialize the counter: += 1
Print the total
"""
help(sum5000)

total = 0
num = 1
while num <= 5000:
    total += num
    num +=1
print('The sum of total integers 5000 is', total)

input('Press any key to exit') 
