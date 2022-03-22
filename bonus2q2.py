x = int(input('Enter an integer: '))
y = int(input('Enter an integer: '))
z = int(input('Enter an integer: '))

if x > y and x > z or x == y > z:
    print(f'{x} is the max')
elif y > x and y > z:
    print(f'{y} is the max')
else:
    print(f'{z} is the max')

