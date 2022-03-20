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

# in-class exercise
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



