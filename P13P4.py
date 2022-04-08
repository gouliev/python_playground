def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print('In function f: ')
    x += 1
    y = 1 #y bring 1, replaces anything else if function invoked and var y is called
    print('x is', x)
    print('y is', y)
    print('z is', z)
    return x

help(f)

x, y, z = 5, 10, 15

print('Before function f: ')
print('x is', x)
print('y is', y)
print('z is', z)

z = f(x) #giving z the value of f(x)

print('After function f: ')
print('x is', x) 
print('y is', y)
print('z is', z)
