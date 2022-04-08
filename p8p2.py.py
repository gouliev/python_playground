def psuedocode():
    """
Prompt the user to input a value, this will be the table size
Create variables for multiplying integers (i and j)
Format table
Set counts
Create while loop to initiate if i <= to table size
Create j <= i
Incremental change
Print result

"""
help(psuedocode) 


size_of_table = int(input('Please enter a number: ')) #size of the table
k = 1
while k <= size_of_table:
    n = 1
    while n <= size_of_table:
        print(k * n, end="\t") #format table using this seperator function
        n = n + 1  #same as +=1
    print()
    k = k + 1 #same as +=1


print('Finished!')
input('Press any key to exit!')
