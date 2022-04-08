def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print('In function f: ')
    x += 1 #+1
    y = 1 #y bring 1, replaces anything else if function invoked and var y is called
    z = 2
    i -+ 1 #-1
    j = 3
    print('x is', x)
    print('y is', y)
    print('z is', z)
    print('i is', i) 
    print('j is', j)
    print('k is', k)
    return x

help(f)

x, y, z, i, j, k = 5, 10, 15, 20, 25, 30

print('Before function f: ')
print('x is', x)
print('y is', y)
print('z is', z)
print('i is', i) 
print('j is', j)
print('k is', k)

j = f(x) #giving z the value of f(x)

print('After function f: ')
print('x is', x) 
print('y is', y)
print('z is', z)
print('i is', i) #+3
print('j is', j)
print('k is', k)
