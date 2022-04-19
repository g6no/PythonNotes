'''
Ahmad Alqattan
2192131011
Homework 2
Question 1
'''

userNum = int(input("Enter a number "))
sumOfFactors = 0

for i in range(1,userNum):
    if userNum % i == 0:
        sumOfFactors += i

if userNum == sumOfFactors:
    print(f'{userNum} is a perfect number')
else:
    print(f'{userNum} is not a perfect number')