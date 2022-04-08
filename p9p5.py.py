def psuedocode():
    """
I was a little stuck on this one, I asked Patrick from CS Support to give me advice
He helped me think about it in psudeocode
3 Loops to generate n!, k!, and n-k! as three separate variables   
N as an input and k as an input, and then proceed to the three loops
n = input
k = input
loop1 (gets you n!)
loop2 (gets you k!)
loop3 (gets you (n-k)!)
Then complete the calculation with your new variable
C(n,r)=
C(n,r)=C(6,4) = example 15

    """
help(psuedocode)


counter_1 = 1
counter_2 = 1
counter_3 = 1

n = int(input('Please input number of possible toppings: '))
k = int(input('Please input number of toppings offered: '))

r = n - k

if n <=0 or k <= 0:
    print('Please enter a positive integer!')

for i in range(1, n + 1):
    counter_1 = counter_1 * i

for m in range(1, k + 1):
     counter_2 = counter_2 * m

for j in range(1, r + 1):
    counter_3 = counter_3 * j

x = counter_1 // (counter_2 * counter_3)

print("The possible combinations are: "+ (str(x)))
