'''
Ahmad Alqattan
2192131011
Bonus 4
'''

response = [1, 1, 3, 4, 3, 3, 5, 4, 1, 2, 4, 5, 3, 2, 5, 5, 2, 1, 4, 5]

sums = [0,0,0,0,0]

for item in response:
    sums[item-1] += 1

print('Rating\tFrequency')
for i in range(1,6):
    print(f'{i}\t{sums[i-1]}')