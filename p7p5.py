def p7p5():
    """
Write a program that sums the integers in the range 1–10 000 that are divisable by 3 or by 5 and
prints out the total.
Create a limit
Create a num
Create a counter for them
I used num + 1 instead of +=
I then used a similar method to P7p5
E.g. num % 5 and num % 3
Then made a summer, where total = total + num(1)
"""
help(p7p5)

limit = 10000
num = 1
total = 0
while num <= limit:
    if num % 3 == 0:
        #print('This number is divisable by 3...')
        total = total + num
        #print('It is NOT divisable by 3')
    elif num % 5 ==0:
        total = total + num
        #print('This number is divisable by 3...')
        #print('It is NOT divisable by 3')
    num = num + 1

print('This is the total sum of numbers 1...10000 which are divisable by 3 and 5:')
print()
print(total)

