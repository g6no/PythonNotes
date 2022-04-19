'''
Ahmad Alqattan
2192131011
Bonus 3
'''

sum = 0
n = input('Enter: ')
while n != '.':
    n = int(n)
    if n % 2 != 0:
        n = input('Enter: ')
        continue
    sum += n
    n = input('Enter: ')
print(sum)