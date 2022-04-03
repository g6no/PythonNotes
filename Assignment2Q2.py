'''
Ahmad Alqattan
2192131011
Homework 2
Question 2
'''

numOfYears = int(input('Enter the number of years: '))
totalRainFall = 0
for i in range(1,numOfYears+1):
    print(f'for year {i}:')
    for i in range(12):
        rainNum = float(input('Enter the rainfall amount for the month: '))
        totalRainFall += rainNum

print(f'For {12*numOfYears} months')
print(f'Total rainfall: {totalRainFall:.2f} inches')
print(f'Average monthly rainfall: {totalRainFall/(numOfYears*12):.2f} inches')