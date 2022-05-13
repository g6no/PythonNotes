'''
Ahmad Alqattan
2192131011
Homework 4
Question 2
'''

jup_moons_rad = {'Io':1821.6, 'Europa':1560.8, 'Ganymede':2634.1, 'Callisto':2410.3}
jup_moons_grav = {'Io':1.796, 'Europa':1.314, 'Ganymede':1.428, 'Callisto':1.235}
jup_moons_orb = {'Io':1.769, 'Europa':3.551, 'Ganymede':7.154, 'Callisto':16.689}

moon_name = input('Enter name of Galilean moon of Jupiter (Io, Europa, Ganymede, Callisto): ')
moon_name = moon_name.lower()
moon_name = moon_name.capitalize()

if moon_name in jup_moons_rad:
    print(f'Details of {moon_name} are:')
    print(f'Mean Radius: {jup_moons_rad[moon_name]} km')
    print(f'Surface Gravity: {jup_moons_grav[moon_name]} m/s\u00b2')
    print(f'Orbital Period: {jup_moons_orb[moon_name]} days')
else:
    print(f'{moon_name} is an invalid moon name.')

