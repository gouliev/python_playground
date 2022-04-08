import math
side = float(input('Enter side: '))
square_area = (side * 2)
cube_vol = (side**3)
circle_area = (math.pi * side**2)
sphere_vol = ((4/3) * math.pi * side**3)
cylinder_vol = (side * math.pi * side**2)

if side <= 0:
    print('Length must be >= 0. Please try again.')
elif side > 0:
    print('The area of a square with side of that lenght', square_area)
    print('The volume of a cube with side of that length', cube_vol)
    print('The area of a circle with side of that length', circle_area)
    print('The volume of a sphere with radius of that length', sphere_vol)
    print('The volume of a cylinder with radius and side of that length', cylinder_vol)

input('Press any key to continue... ')
