import os

filename = input('Enter the file name: ') #check if you can use ,r within the input
if not os.path.isfile(filename):
    print('File' + filename + ' does not exist.')

with open (filename, 'r') as file: #context manager
    a = ['(', ')']
    b = ['[', ']']
    c = ['<', '>']
    d = ['{', '}']
    if a in filename:
        print('Found', a.count())
    if b in filename:
        print('Found', b.count())
    if c in filename:
        print('Found', c.count())
    if d in filename:
        print('Found', d.count())
    if a.count % 2 == 0:
        print('Even number')
    else:
        print('Odd number')
    if b.count % 2 == 0:
            print('Even number')
    else:
        print('Odd number')
    if c.count % 2 == 0:
            print('Even number')
    else:
        print('Odd number')
    if d.count % 2 == 0:
            print('Even number')
    else:
        print('Odd number')