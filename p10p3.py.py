def first_attempt_failed():
    """
First create stored variables for VOWELS
Loop statement for input
CONDITION statements if entered in string
Break if else
Counter initiated
Print output if string contains vowel
USE for loop for this.

"""

help(first_attempt_failed)

a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
vowels = "aeiou"

#created counter for each of the above, but eventually just used the vowels = 'aeiou' instead
count_for_a = 0
count_for_e = 0
count_for_i = 0
count_for_o = 0
count_for_u = 0

while True:
    sentence = input('Enter a string to check its vowel count: ')
    string = sentence.lower() #lowercases the string incase user inputs capitalized letters
    if a in sentence:
        count_for_a +=1
    if e in sentence:
        count_for_e +=1
    if i in sentence:
        count_for_i += 1
    if o in sentence:
        count_for_o +=1
    if u in sentence:
        count_for_i +=1
    for i in vowels:
        print(i, sentence.lower().count(i)) #This method worked better, it printed sentence and used count function and also lower capitalized it
input('Press key to exit')
   
print('Number of total A is, ', count_for_a )
print('Number of total E is, ', count_for_e )
print('Number of total I is, ', count_for_i )
print('Number of total O is, ', count_for_o )
print('Number of total U is, ', count_for_u ) 
