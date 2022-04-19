'''
Ahmad Alqattan
2192131011
Homework 1
Question 2
'''

print(format(0.5, '.0%'))

numOfMales = int(input('Enter the Number of Males in the Class: '))
numOfFemales = int(input('Enter the Number of Females in the Class: '))

totalClass = numOfMales + numOfFemales

print('The class is', format(numOfMales/totalClass, '.0%'), 'Males and',
      format(numOfFemales/totalClass, '.0%'), 'Females')
