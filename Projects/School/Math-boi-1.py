# sqside = float(input('What be the length of the side of yer square? '))
# sqarea = sqside * 2
# print(f'The area of your square is {sqarea}')

# import math
# pi = math.pi
# cirrad = float(input('What be teh radius of yer circle? '))
# cirarea = cirrad * pi
# print(f'The area of your circle is {cirarea}')

# reclength = float(input('What be teh length of yer rectangle? '))
# recwidth = float(input('What be teh width of yer rectangle? '))
# recarea = reclength * recwidth
# print(f'The area of your rectangle is {recarea}')

import math
pi = math.pi
length = float(input('Giveth a length '))
sqarea = length * 2
cirarea = length * pi
cubvol = length ** 3
sphvol = ((4/3) * (pi) * (length ** 3)) 
print(f'The area of the square is {sqarea}')
print(f'The area of the circle is {cirarea}')
print(f'The volume of the cube is {cubvol}')
print(f'The volume of the sphere is {sphvol}')