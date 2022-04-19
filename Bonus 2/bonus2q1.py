userAge = int(input('Please Enter your age: '))

if userAge >= 18:
    print('You can vote')
elif userAge == 17:
    print('You can learn to drive')
elif userAge == 16:
    print('You can buy a lottery ticket')
else:
    print('You can go Trick-or-Treating')
