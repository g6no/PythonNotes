'''
Ahmad Alqattan
2192131011
Homework 4
Question 1
'''
import math


def read_data():
    n = int(input('How many students do you have? '))
    totals = []
    for i in range(n):
        grade = int(input('Enter a total: '))
        grade /= 10
        grade = math.floor(grade)
        grade *= 10
        totals.append(grade)
    return totals

def count_frequency(totals):
    grades = {90: 'A', 80: 'B', 70: 'C', 60: 'D', 50: 'F'}
    grade_count = {'A': 0, 'B':0, 'C':0, 'D':0, 'F':0}
    for total in totals:
        if total >= 50:
            grade_count[grades[total]] += 1
        else:
            grade_count['F'] += 1
    return grade_count


def print_table(count):
    print('Grade Frequency')
    for grade in count:
        print(f'{grade}\t{count[grade]}')


def print_chart(count):
    for grade in count:
        print(f'{grade}: {"*"*count[grade]}')


total = read_data()
grade_count = count_frequency(total)
print()
print_table(grade_count)
print()
print_chart(grade_count)

