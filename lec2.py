# # #Lecture 2 python Dr.Lulwah
#
# print("I'm Ahmad")
# print('The book is "starting python"')
# print('''I'm Ahmad and I'm using "starting python"''')
# print("""I'm Ahmad and I'm using "starting python""")
#
# print("""One
# Two
# Three""")
#
# # #equivalent statements
#
# print("One")
# print("Two")
# print("Three")
#
# #equivalent statements
#
# print("One\nTwo\nThree")
#
# '''
# This is a comment
# Hello
# Hi
# Heellloooo
# Ello
# '''
#
#
# room = 503
# print('I am staying in room number', room)
# #Items are automatically seperated by a space when displayed on screen
#
#
# #####################                               Lecture 3 Python                                ######################
# dollars = 2.75
# print('I have in my account', dollars)
# print('I have in my account %s' %dollars) #different ways to print variables in python
# print('I have in my account {}'.format(dollars))
#
# # print(type(1)) #<class 'int'>
# # print(type(dollars)) #<class 'float'>
#
# # print('Hello', input('Hello'))
# firstName = input('Enter your first name: ')
# lastName = input('Enter your last name: ')
#
# print('Your full name is', firstName, lastName)
# print('Your full name is %s %s' %(firstName,lastName))
# print('Your full name is {} {}'.format(firstName, lastName))
#
# #input returns a string, to get an int or flot, we wrap the input function with the type function
#
# name = input('What is your name?')
# age = int(input('What is your age?'))
# income = float(input('What is your income?'))
#
# print(2**3**4)
# print((2**3)**4)
# print(2**(3**4))
#
# my_num = 5 * 2.0
# print(my_num)
#
# f = 2.6
# print(int(f))
#
# x = -2.9
# print(int(x))
#
# # to break long statements into multiple lines in python
# var1 = 1
# var2 = 2
# var3 = 3
# var4 = 4
# result = var1 * 2 + var2 * 3 + \
#     var3 * 4 + var4 * 5 # example
#
# print(result)
# # also, anything inside parentheses can be broken into multiple lines
# print("Monday", "Tuesday",
#       "Wednesday", "Thursday",
#       "Friday")
#


#####################                               Lecture 4 Python                                ######################

# #print function
# num = 201
# print('CpE',num)
# print('CpE',num, end = '*', sep = ':')
# print('CpE',num, sep= '%') #doesn't move to new line since we changed the end in previoud print statement
#
# print('one', end = '=') # in here there is no space between one and = since it is not considered an argument
# print('two')
# print('one', 'two', 'three', sep = '?')
#
# # Escape characters
# print('Ahmad\nHasan\tAl\'qa\"tt\\an')
#
# print('I\'m Ahmad')
# print("The book pf \"Python\"")
# print('hello \\\'Lulwah\"')
# print('Is this \\\ right?')
#
# # + addition if numeric and string concatenation if string
# print('One'+'Two'+'Three')
#
# num = 300
# print('One is ' + str(num))
# #print('One is ' + num) error
#
#
# # Formatting floating-point numbers
# amount_due = 5000.0
# monthly_payment = amount_due/12
# print('The monthly payment is',format(monthly_payment, '.2f'))
#
# monthly_pay = 5000.0
# annual_pay = monthly_pay * 12
# print('Your annual pay is $', format(annual_pay,',.2f'), sep = '') #Your annual pay is $60,000.00
#
#
# # Formatting Minimum Field Width
# num1 = 127.899
# num2 = 3465.148
# num3 = 3.776
# num4 = 264.821
# num5 = 88.081
# num6 = 799.999
#
# print(format(num1, '9.2f'))
# print(format(num2, '9,.2f')) # to add a comma after every 3 digits
# print(format(num3, '9.2f'))
# print(format(num4, '9.2f'))
# print(format(num5, '9.2f'))
# print(format(num6, '9.2f'))
#
# print(format(0.5, '.0%'))

# print('The first cold shower\neven the monkey seems to want\na little coat of straw')
#
# print('''The first cold shower
# even the monkey seems to want
# a little coat of straw''')


# print('Hi! I\'m Eli.')
# print('The title of the book was \\\"Good Omens\\\".')
# print('Hi! I\\\'m Sebastien.')


#####################                               Lecture 5 Python                                ######################

# Magic numbers are unexplained numbers appearing in code
# (amount = balance * 0.069) --> in this example, 0.069 is unknown to signify what

# To avoid this, we use named constants, whose value does not change throughout the program
# INTEREST_RATE = 0.069
# Naming convention for named constants --> all upper case
# amount = balance * INTEREST_RATE

# if statements in python
# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

# Comparing strings:
# string1 == (!=) string2 to check if the string equals or does not equal

# comparison operators on strings: compare using >, <, >=, <=
# compares characters using ASCII values, same as alphabetical order if same case

# print('y'>'k') returns True
# print('y'>'z') returns False

# print('Max' > 'Last') returns True

# min_salary = 30000.0
# min_years = 2
#
# salary = float(input('Enter annual salary: '))
# years_on_job = int(input('Enter years on job: '))
#
# if salary >= min_salary:
#     if years_on_job >= min_years:
#         print('qualify')
#     else:
#         print('More years')
# else:
#     print('You must earn at least $', format(min_salary, ',.2f'), ' per year to qualify', sep='')

# output:
# Enter annual salary: 20000
# Enter years on job: 2
# You must earn at least $30,000.00 per year to qualify

# Memory:
# min_salary -> 30000
# min_years -> 2
# salary -> 20000
# years_on_job -> 2

# score = float(input('Enter your score: '))
#
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# elif score >= 0:
#     print('F')
# else:
#     print('Invalid')


# # Using nested if statements
# if score >= 90:
#     print('A')
# else:
#     if score >= 80:
#         print('B')
#     else:
#         if score >= 70:
#             print('C')
#         else:
#             if score >= 60:
#                 print('D')
#             else:
#                 print('F')


#####################                               Lecture 6 Python                                ######################
# using elif

# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

# And operator
# raining = False
# temp = 0
#
# if temp < 20 and raining == True:
#     print('Cold')
# else:
#     print('Not Cold')

# Output: Not Cold

# Or operator
# raining = False
# temp = 0
#
# if temp < 20 or raining == True:
#     print('Cold')
# else:
#     print('Not Cold')

# Output: Cold

# not operator
# raining = False
# if not(raining):
#     print('Not Raining')

# Output: Not Raining


# Checking numeric range and simplified chain comparison

# x = 15
# if x >= 10 and x <= 20:
#     print('in range')

# if 10 <= x <= 20: #using this type of expression is allowed in python
#     print('in range')


# chain comparison
# x = 5
# 0 <= x <= 5
# result: True
# 0 <= x <= 5 > 1
# result: True
# 0 <= x <= 5 > 5
# result: False

# x = 3
# print(0 <= x <= 5 < 5) #incorrect expression
# print(0 <= x <= 5 and x < 5)

# x = 3
#
# if x:
#     print('True')
# x = 0
# if x:
#     print('True')
# else:
#     print('False')
# will print as long as x != 0

# userColor = input('Enter your favorite color: ')
#
# if userColor.lower() == 'red':
#     print('I like Red too')
# else:
#     print(f'I don\'t like {userColor}, I prefer red')

# firstNum = int(input('Enter first num: '))
# secondNum = int(input('Enter second num: '))
#
# if firstNum % secondNum == 0:
#     print('%s multiple of %s' %(secondNum, firstNum))
# else:
#     print('%s not a multiple of %s' %(secondNum, firstNum))
#
# if not(firstNum % secondNum):
#     print('%s multiple of %s' % (secondNum, firstNum))
# else:
#     print('%s not a multiple of %s' % (secondNum, firstNum))


# bonus, extra q: Ask the user to enter a number between 10 and 20(inclusive)
# If they enter a number within the range display "Thank you", otherwise
# display 'Incorrect Message'

# userNum = int(input('Enter a number between 10 and 20: '))
#
# if 10 <= userNum <= 20:
#     print('Thank you')
# else:
#     print('Incorrect Message')

#####################                               Lecture 7 Python                                ######################
# Two types of repetition structures:
# 1- condition controlled loop (either true or false) --> while loop
# 2- count controlled loop (for i in range(n)) --> for loop

# while loop works on a pre-test condition, which it tests before executing the statements inside the loop

# count = 10
# while count < 1:
#     print('Hello World')

# in this example, nothing will be printed

# in-class exercise 1
# userNum = int(input('Enter an integer, or -1 to exit: '))
# userMax = userNum
#
# while userNum != -1:
#     if userMax < userNum:
#         userMax = userNum
#     userNum = int(input('Enter an integer, or -1 to exit: '))
#
# if userMax != -1:
#     print(userMax)
# else:
#     print('No input')

# in this example, -1 is a sentinel value
# sentinel values inform the user how to exit the loop
# sentinel values have to be logical (intuitive), e.g.: if asking for weights,
# sentinel value can be 0 since no one weighs 0 Kg


# in-class exercise 2
# for i in range(11):
#     if i % 2 == 0:
#         print(i, end=' ')
# print('\n')
#
# for i in [0, 2, 4, 6, 8, 10]:
#     print(i,end=' ')
# print('\n')

#####################                               Lecture 8 Python                                ######################

# for name in ['Winken', 'Blinken', 'Nod']:
#     print(name)

# printing all even numbers from 0 to 100 is difficult, that's why we use a range function
# for i in range(101):
#     if i % 2 == 0:
#         print(i, end=' ')
# print('\n')

# range function syntax:
# keep in mind, end vlaues not included
# One arguement: ending limit, default start = 0, default step 1
# Two arguements: start and end values, default step 1
# Three values: start, end , step

# for num in range(-1):
#     print(num)
#     no result in this case, doesnt enter the loop

# for num in range(10,1,-1):
#     print(num)

# for num in range(1,10,2):
#     print(num)

# num = 1
# while num < 10:
#     print(num)
#     num += 2

# in class exercise:
# START = 60
# END = 130
# INCREMENT = 10
# FACTOR = 0.6214
#
# print('KPH\tMPH\n----------------')
# for kph in range(START, END+1, INCREMENT):
#     mph = kph * FACTOR
#     print(f'KPH = {kph}\tMPH = {mph:.2f}')
#
# kph = START
# while kph <= END:
#     mph = kph * FACTOR
#     print(f'KPH = {kph}\tMPH = {mph:.2f}')
#     kph += INCREMENT

#####################                               Lecture 9 Python                                ######################

# Multiple assignment
# a, b = 1, 3
# print(a, b)

# computer can't tell the difference between good and bad data
# we solve this problem by validating the input through a loop
# GIGO: garbage input --> garbage output

# example:
# Get a test score
# score = float(input('Enter the test score'))
#
# while score < 0 or score > 100:
#     score = float(input('Invalid Input, enter the correct score'))

# for hour in range(24):
#     for minute in range(60):
#         for sec in range(60):
#             print(f'{hour}:{minute}:{sec}')

# number of total iterations = 24 * 60 * 60

# numOfStudents = int(input('Total Number of Students: '))
# numOfTests = int(input('Total Number of Tests per students: '))
#
# for i in range(1, numOfStudents + 1):
#     totalSum = 0
#     for j in range(numOfTests):
#         totalSum += float(input('Test Score: '))
#     print(f'The average for student number {i} is {totalSum/numOfTests}')


#####################                               Lecture 9 Python                                ######################

# y = 100
# while y > 0:
#     print(y)
#     y = y + 1
# error infinite loop, change to y = y + 1

# i = 0
# while i < 5:
#     j = 1
#     while j <= 2:
#         j = j + 1
#     i += j + 1
#
# print(i)
# output: 8

# while loops can have an else statement
# when the loop finishes ender normal conditions, the else statements are executed
# i = 0
# while i < 4:
#     i +=1
#     print(i)
# else:
#     print('Loop finished')

# break statement
# will immediately exit the loop when executed
# it will also skip the else statement

# x = 3
# while x < 5:
#     print(x)
#     x += 1
# else:
#     print('Done')
# x = 3
# while x < 5:
#     print(x)
#     x += 1
#     print('Done')
# x = 3
# while x < 5:
#     if x == 4:
#         break
#     print(x)
#     x += 1
# else:
#     print('Done')

# x = 1
# while x <= 10:
#     if x == 5:
#         break
#     print(x)
#     x += 1

# this while loop will stop when x = 5

# write random number and make a guessing game
# import random
#
# randNum = random.randint(0, 100)
# print(randNum)
# userNum = int(input('Guess a number: '))
#
# while 0 <= userNum <= 100:
#     if userNum > randNum:
#         print('Guessed too high.')
#     elif userNum < randNum:
#         print('Guessed too low.')
#     else:
#         print(f'You guessed it. The number was: {randNum}')
#         break
#     userNum = int(input('Guess a number: '))
# else:
#     print(f'You quit early, the number was {randNum}')


# Another solution without break
# randNum = random.randint(0, 100)
# print(randNum)
# userNum = int(input('Guess a number: '))
#
# while 0 <= userNum <= 100 or userNum != randNum:
#     if userNum > randNum:
#         print('Guessed too high.')
#     elif userNum < randNum:
#         print('Guessed too low.')
#     userNum = int(input('Guess a number: '))
# else:
#     if userNum != randNum:
#         print(f'You quit early, the number was {randNum}')
#     else:
#         print(f'You guessed it. The number was: {randNum}')


# do while loops in python
# age = int(input('Age: '))
# while age >= 1:
#     age = int(input('Age: '))
#
# # Solution: using while True:
# while True:
#     age = int(input('Age: '))
#     if age < 1:
#         break

# do while in c++
#     do{
#     statement
# } while(condition);

# continue in python
# it will skip the code below it and goes back to the start

# for x in range(1,10+1):
#     if x == 5:
#         continue
#
#     print(x)

# sum = 0
# while True:
#     userNum_str = input('Enter a number: ')
#     if userNum_str == '.':
#         break
#     else:
#         userNum = int(userNum_str)
#         if userNum % 2 == 0:
#             sum += userNum
# print(sum)


# exercise on break inside nested while loops
# x = 3
# y = 4 y = 3 y = 2
# x = 2
# y = 2
# x = 1
# y = 2
# x = 3
# y = 4

# while x > 0:
#     print('\nx =', x)
#
#     while y > 0:
#         print('y =', y, end=' ')
#         if y == 2:
#             break
#         y -= 1
#     x -= 1

# Solution using continue instead of break
# sum = 0
# n = input('Enter: ')
# while n != '.':
#     n = int(n)
#     if n % 2 != 0:
#         n = input('Enter: ')
#         continue
#     sum += n
#     n = input('Enter: ')
# print(sum)

# Function: group of statements within a program that preforms a specific task
# Modularized program: program wherein each task within the program is in
# its own function

# Two type of functions:
# 1- A void function
# - void function = procedure: doesn't return output
# 2- value returning function: returns output

# Defining a function and calling it
# def function_name():
#     statement
#     statement

# function name should include a verb

# example function
# def print_message(message):
#     print(message)
#
#
# print_message('Hello')

# function definition has to be above the function call

# main function: called when the program starts
# calls other functions when they are needed and
# defines the mainlines logic of the program

# main function example
# def main():
#     print('I have a message for you.')
#     message()
#     print('Goodbye!')
#
# def message():
#     print('I am Arthur')
#     print('King of the Britons')
#
# main()

# Each block of code must be indented

# Value-returning functions can be useful in specific situations

# def IsEven(num):
#     isEven = True
#     if num % 2 != 0:
#         isEven = False
#     return isEven
#
#
# n = int(input('Enter a number: '))
# if IsEven(n):
#     print('The number is even')
# else:
#     print('The number is odd')

#####################                               Lecture 10 Python                                ######################

# def ReturnDigit(x, position):
#     x = str(x)
#     return int(x[len(x)-position])
#
# y = ReturnDigit(7392564, 5)
# print(y)

# def get_digit_position(num, position):
#     my_digit = num // (10 ** (position - 1)) % 10
#
#     return my_digit
#
# num = int(input('Enter an integer: '))
# position = int(input('Enter the position: '))
#
# print('The digit at', position, 'is:', get_digit_position(num, position))

def show_interest(interest, rate, periods):
    print(interest*rate*periods)

show_interest(10,10, rate=10)
