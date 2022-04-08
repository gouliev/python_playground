def p8p3():
    """
 x x (horizontal)
 x x (vertical)
 
INPUT for size of table
Create TRUE condition if INPUT greater than limit
LIMIT = 20
SET size of table > 20 condition
BREAK if larger value entered
ELSE.. continue with variables K, N
Create a heading (Times Table)
Print function to multiply k * n
Set count (augmented assignment +=1)
N = column size, i.e. 2x2 column row
Print finish
Break so no loop for multiple series requests (not mentioned to prompt series)

"""
help(p8p3)

size_of_table = int(input('Please enter a number: ')) #size of the table
while True: 
    if size_of_table > 20: 
        print('Please try again with a integer less than 20')
        break
    else:
        k = 1
    print('Times', size_of_table, 'Table')
    while k <= size_of_table:
        n = 1
        while n <= 2:
            print(k * n, end="\t") #format table using this seperator function
            n = n + 1  #same as +=1
        print()
        k = k + 1 #same as +=1
    break
        
print('Finished!')
input('Press any key to exit!')



