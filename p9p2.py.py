def psuedocode():
    """
CREATE true condition
CREATE input variable
SET to <=0 (break if broken)
Else condition
Set count
USE for in range
Include the input into the sum
Print result
"""
help(psuedocode)

while True:
    taking_input = int(input('Please enter a positive integer: '))
    if taking_input <= 0:
        break
    else:
        x = 0
        for i in range(1, taking_input + 1):
            x += i
            print(i)
    print(x)

print('Finished')
