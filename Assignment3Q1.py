'''
Ahmad Alqattan
2192131011
Homework 3
Question 1
'''

from datetime import date


def main():
    while True:
        userName = input('Enter your name: ')
        if userName  == '.':
            break
        userDOB = input('Enter your date of birth (dd/mm/yyyy): ')
        if userDOB == '.':
            break
        userHeight = input('Enter your height in meters: ')
        if userHeight == '.':
            break
        userWeight = input('Enter your weight in Kg: ')
        if userWeight == '.':
            break
        age = computeAge(userDOB)
        print(f'\n{userName}\'s age is {age}')
        maxHr = computeMHR(age)
        print(f'Your maximum heartrate is {maxHr}')
        bmi = computeBMI(userWeight,userHeight)
        cat = checkCat(bmi)
        print(f'Your BMI is {bmi:.2f} --> {cat}\n')

    print('\nThank you for using the program!')

def computeAge(userDOB):
    day, month, year = map(int, userDOB.split('/'))
    userDate = date(year, month, day)
    today = date.today()
    # the first part deducts the current year from the user inputted year of birth
    # second part checks if the current month and day is less than the user inputted month and day,
    # if true, that part becomes equal to 1 and subtracts 1 from the first operation
    age = (today.year - userDate.year) - ((today.month, today.day) < (userDate.month, userDate.day))
    return age


def computeMHR(age):
    return 220 - age


def computeBMI(weight, height):
    weight = float(weight)
    height = float(height)
    bmi = weight / height **2
    return bmi


def checkCat(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 24.9:
        return 'Normal'
    elif bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'


main()
