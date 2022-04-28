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

# def show_interest(interest, rate, periods):
#     print(interest*rate*periods)
#
# show_interest(10,10, rate=10)


#####################                               Lecture 11 Python                                ######################
# Named parameters are a way to give default values to parameters

# def box (height = 10, width = 10, length = 10):
#     print(height, width, length)

# read Named and default arguements/parameters

# (3,7,10)
# (25, 5, 24)
# (100, 5, 50)
# error

# def func(a, b=5, c=10):
#     print(a, b, c)
#
#
# func(3, 7) --> 3 7 10
# func(25, c=24) --> 25 5 24
# func(c=50, a=100) --> 100 5 50
# func(c = 50) #--> ERROR, a value is missing

# Global variable

# my_value = 10
#
# def show_value():
#     print(my_value)
#
# show_value() # --> Prints 10

# number = 10
#
# def main():
#     global number
#     number = int(input('Enter a number: '))
#     show_number()
#
# def show_number():
#     print("The number is", number)
#
# main()

# we use global to change the value of a global variable

# x = 5
# y = 4
#
# def sum_xy():
#     x = x + 3
#     print(x+y)
#     error  here since x is not defined
#
# sum_xy()


# x = 5
# y = 4
#
# def sum_xy():
#     global x
#     x = x + 3
#     print(x+y)
#
# print(x) # --> x = 5
# sum_xy() # --> 12
# print(x) # --> x = 8
# because the x changed after the function call

# x = 5
# y = 4
#
# def sum_xy():
#     x = y + 3
#     print(x+y)
#
#
# sum_xy()
# print(x,y)

# import random
# random.seed(10)
# for i in range(10):
#     result = random.randint(1,2)
#     print(result)
#     if result == 1:
#         print('Heads')
#     else:
#         print('tails')


# import can also be written by using: from random import *, from random import randint

# we use random.seed(int) at the start of the program, and it fixes

#####################                               Lecture 12 Python                                ######################
# nothing


#####################                               Lecture 13 Python                                ######################

# Sequence: an object that contains multiple items of data
# Python Sequence types;
# - List (mutable)
# - tuples (immutable)
# - strings (immutable)

# List: an object that contains multiple date items
# list = [item1, item2, 3, 4.0]
# can contain different types

# for item in list:
#     print(item) #this will print every item in a list on a seperate line

# for i in range(len(list)):
#     sum += list[i]
#
# this accesses every variable in a list by index


#####################                               Lecture 14 Python                                ######################
# lst = [1,2,3,4]
# lst.append([1,2,3])
# print(lst)

# list1 = [1,2,3]
# list1.extend(4) # error
# list1.append(4) #[1,2,3,4]
# list1.append([4,5,6]) # [1,2,3,[4,5,6]]
# list1.extend([4,5,6]) # [1,2,3,4,5,6]

# list1 = [1,2,3]
# list1.append('xyz') #[1, 2, 3, 'xyz']
# print(list1)
# list1.extend('abc') #[1, 2, 3, 'xyz', 'a', 'b', 'c']
# print(list1)
# list1 += 'max' #[1, 2, 3, 'xyz', 'a', 'b', 'c', 'm', 'a', 'x'] has same function as extend
# print(list1)
# list1 = list1 + 'min'
# print(list1)

# list2 = [1,2,3]
# list3 = [4,5,6]
# list2 += list3
# print(list2)
# list2 = [1,2,3]
# list2 = list2 + list3
# print(list2)

# def main():
#     food = ['Pizza', 'Burgers', 'Chips']
#     print(food)
#
#     item = input('Which item should I change?')
#     try:
#         item_index = food.index(item)
#         new_item = input('Enter the new value: ')
#         food[item_index] = new_item
#         print(food)
#
#     except ValueError:
#         print('item not in list')
#
# main()

# list1 =[1,2,3]
# list1.insert(9,4)
# print(list1)

# insert, if invalid index replace with a valid one withous issuing indexErrorExcpetion

# food = ['Chips', 'Pasta', 'Pizza', 'Pickels']
# food.sort()
# print(food)
# food.sort(reverse=True)
# print(food)
# food.remove('Pizza')
# print(food)
#
# popTeam = food.pop()
# print(popTeam)
# print(food)
#
# food = ['Chips', 'Pasta', 'Pizza', 'Pickels']
# # popTeamEpic = food.pop(0)
# # print(popTeamEpic)
#
# # when using pop and indexing a value, index has to be withing fucntion
#
# del food[2]
# list2 = [1,2,3,4,5,6,9,7]
# print(max(list2))
# print(min(list2))

# n = int(input('Enter the number of numbers: '))
#
# lst = []
# total = 0
# for i in range(n):
#     num = int(input(f'Enter number {i+1}: '))
#     total += num
#     lst.append(num)
#
# print(lst)
# print(total/len(lst))

# x =[1,2,3,4,5]
# y = [8,6,10,7,9]
# z = []
#
# x.append(6) #a
# y.sort()
# x.extend(y)
# print(x)
# z = [1] * 5
# print(z)
# for i in range(5):
#     z.append(2)
# print(z)
# print(sum(z))
# z.insert(5,3)
# print(z)
# x.extend(z[4:7])
# print(x)
# print(min(x))
# print(max(x))
# x.remove(1)
# print(x)

# import random
#
# x = random.randrange(1,10)
#
# while x != 10:
#     print(x)
#     x = random.randrange(1, 10)

# if 'hello' not in 'hello everyone':
#     print('hkime')

#####################                               Lecture 15 Python                                ######################
# list1 = [1,2,3,4]
# list2 = list1
#
# print(list1)
# list2.append(5) --> both of these variables point to the same values, so a change in one is a change in both
# print(list1)

# to create a copy of a list, either use a for loop or use concatenation
# list1 = [1,2,3,4]
# list2 = []
# for item in list1:
#     list2.append(item)
#
# or
#
# list1 = [1,2,3,4]
# list2 = [] + list1

# my_int = 27
# your_int = my_int
# print(your_int)
# your_int = 3
# print(your_int)
# print(my_int)
# this does not cause a problem, since integers are immutable, while lists are mutable
# the change (assignment) creates a copy of the object, and does not change the original value

# my_list = [1,2,3]
# newLst = my_list[:]
# newLst.append(4)
# print(my_list)
# this is a suitable way to copy single-dimensional lists

# a_list = [1,2,3]
# b_list = [5,6,7]
# a_list.append(b_list)
# b_list.append(10)
# print(a_list)

# this is called a shallow copy, since it uses the reference

# if we want a full copy, we can use deepcopy
# import copy
# alist = [1,2,3,4]
# blist = copy.deepcopy(alist)

# a  = [1,2,3,[4,5]]
# b = []
# for item in a:
#     if type(item) != "<class list>":
#         b.append(item)
#     else:
#         c = []
#         for elem in item:
#             c.append(elem)
#         print(c)
#         b.append(c)
#     print(b)
# import copy
# a_list = [1,2,3]
# b_list = [5,6,7]
# a_list.append(b_list)
# c_list = copy.deepcopy(a_list)
# b_list[0] = 1000
# print(a_list)
# print(b_list)
# print(c_list)
# the change done on b is not reflected on c, since it is a deep

# two dimensional list, is  a list that contains other lists as an element

# mtrx = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
# for i in range(len(mtrx)):
#     print(f'Enter elements of row {i}')
#     for j in range(len(mtrx[i])):
#         mtrx[i][j] = int(input(''))
#     print(mtrx[i])

# def main():
#     numbers = [2,4,6,8,10]
#     print('The total is', get_total(numbers))
#     print(numbers)
#
# def get_total(val_list):
#     total = 0
#
#     for num in val_list:
#         total += num
#
#     val_list.append(12)
#     return total
#
# main()

# def my_fun(param):
#     param.append(4)
#     return param
#
# my_list = [1,2,3]
# new_list = my_fun(my_list)
# print(my_list, new_list)
# the append inside the function has changed the var my_list, and new_list takes the value of list returned by my_fun


# def my_fun(param):
#     param.append(4)
#     return param
#
# my_list = [1,2,3]
# new_list = my_fun(my_list)
# print(my_list, new_list)
# new_list.extend([7,8,9]) # any change made to the new_list, since it points to the same memory place, will occur in both
# this is because lists are mutables
# print(my_list,new_list)
# the append inside the function has changed the var my_list, and new_list takes the value of list returned by my_fun

# def fn1(arg1 = [], arg2 = 27):
#     arg1.append(arg2)
#     print('arg1',arg1)
#     return arg1
#
# my_list = [1,2,3]
# print(fn1(my_list,4)) # my list changes to [1,2,3,4]
# print(fn1(my_list))  # my list changes to [1,2,3,4,27]
# print('my list', my_list)
# print(fn1()) # returns [27] and arg1 changes to [27]
# print(fn1()) # returns [27,27] and arg1 changes [27,27]

# def func (a, b):
#     b = 20
#     print(a)
#     print(b)
#     a.append(15)
#     print(a)
#     c=a
#     c.append(12)
#     return c
# a=9
# z = [1,2,3,4]
# x = func (z, a)
# print(a)
# print(z)
# print(x)

# arg1 = []
# def fn1(arg1 = [], arg2 = 27):
#     if arg1 == []:
#         arg1 = []
#     arg1.append(arg2)
#     return arg1

# def func2(a):
#     print(a)
#     a.append(15)
#     print(a)
#     c = []
#     for val in a:
#         c.append(val)
#     c.append(12)
#     return c
#
# z = [1,2,3,4]
# x = func2(z)
# print(z)
# print(x)

# output:
# [1,2,3,4]
# [1,2,3,4,15]
# [1,2,3,4,15]
# [1,2,3,4,15,12]


# tuples are immutable sequences

# to create a tuple
# tupl = (1,2,3,4)
# print(tupl)
#
# tupl1 = (1,) # if it has one value, it has to have a trailing comma
#
# tupl2 = tupl + tupl1
# print(tupl2)
#
# myTuple = 1,2
# print(myTuple) # (1,2)
# myTuple = (1,)
# print(myTuple) #(1,)
# myTuple = (1)
# print(myTuple) #(1)
# myTuple = 1,
# print(myTuple) #(1,)

# commas are what create tuples, not the parentheses as we can see

# myTuple = (1,2,3)
# myList = [1,2,3]
# newList = list(myList) #[1,2,3]
# print(newList)
# newTuple = tuple(myList) #(1,2,3)
# print(newTuple)
#
# myTuple = (1,2,3)
# myList = [1,2,3]
# list(myList)
# tuple(myList)
# print(myTuple)
# print(myList)

# def fun(list1,list2):
#     common = False
#     for elem1 in list1:
#         for elem2 in list2:
#             if elem1 == elem2:
#                 return True
#
#     return common
#
#
# def fun2(list1, list2):
#     common = False
#     for elem1 in list1:
#         if elem1 in list2:
#             common = True
#
#     return common
#
# print(fun([1,2,3],[9,8,3]))
# print(fun2([1,2,3],[9,8,3]))

# define a dictionary dic = {key:value, key2:value2}

# keys in dictionaries have to be immutable, so we cant use lists
# values can be anything

# index a dictionary using the key
# print(dic[key]) #prints value
# if key does not exist in dictionary, KeyError is returned


# dict = {'bill':123, (3,5,2):'Hello', 4.5:[1,2,3,4]}
# print(dict[(3,5,2)]) # Hello
# print(dict[4.5]) # [1, 2, 3, 4]

# to add a new key-value pair to a dictionary
# dict['Jacob'] = 'new kv pair' # creates a new pair since Jacob doesn't exist initially
# dict['bill'] = [1, 2, 3] # changes the value of bill
# dict['Sam'] = 2.213 # creates new pair

# print(dict)

# dictionaries are mutable objects that can be changed

# we can delete items from a dictionary
# del dict[key]
# del dict[4.5]
# print(dict) # deletes pair 4.5:[1,2,3,4]
# del dict[4.5]
# print(dict) #k

# we can create an empty dictionary through this syntax
# my_dict = {}
# print(type(my_dict))

# or
# my_dict2 = dict
# print(type(my_dict2))

# when using the len function on a dictionary, it will return the number of key value pairs
# dict = {'bill':123, (3,5,2):'Hello', 4.5:[1,2,3,4]}
# for key in dict:
#     print(key)
#     print(dict[key])

# dict.clear(deletes all elements in a dictionary and leaves it empty)
# dict.get(key, default) return the value associated with key, or default if key doesn't exist
# doesn't return a KeyValue Eroor

# phonebook = {'Haya':123, 'Amal':333}
# print(phonebook)
# phone = phonebook.get('Haya')
# print(phone)
# print(phonebook.get('Hay'))
# print(phonebook.get('Hay', 'Not found'))

# phonebook = {'Haya':123, 'Amal':333, 'Salem':345, 'May':123}
# print(phonebook)
# my_dictionary_view = phonebook.items()
# print(my_dictionary_view) # returns them as a tuple dict_items([('Haya', 123), ('Amal', 333), ('Salem', 345), ('May', 123)])
# for key, value in my_dictionary_view:
#     print(key, value)

# for key in my_dictionary_view:
#     print(key, my_dictionary_view[key]) # error, TypeError: 'dict_items' object is not subscriptable
#
# for key in my_dictionary_view:
#     print(key) # ('Haya', 123)
#                ('Amal', 333)
#                ('Salem', 345)
#                ('May', 123)
# Prints
# Haya 123
# Amal 333
# Salem 345
# May 123


#####################                               Lecture 16 Python                                ######################

# dict = {'Ali':123, 'Lulwah':456, 'Ahmad':212, 'Sara':234}
# print(dict) #{'Ali': 123, 'Lulwah': 456}
# keys = dict.keys()
# print(keys) # dict_keys(['Ali', 'Lulwah'])
#
# for key in keys:
#     print(key)
#
# for key in dict:
#     print(key)

# print(dict.pop('Sara'))
# print(dict)
# print('+', dict.pop('Sara', 'None')) # It has to have a default, if not then keyError
# print(dict)
# print(dict.get('Sara'))
# pop has to have a default value, but get if no default is specified return None
# pop returns value associated with key, and removes the pair from the dictionary

# popitem removes a random key-value pair from the dictionary, but usually removes the last item in dictionary
# values returns all the dictionary values as a sequence

# phonebook = {'Haya':123, 'Amal':333, 'Salem':345, 'May':123, 'Ahmad':345}
# print(phonebook)
# phone_num = phonebook.pop('Amal', 'Not Found')
# print(phone_num)
# print(phonebook)
# phone_num = phonebook.pop('Laila', 'Not Found')
# print(phone_num)
# print(phonebook)
# k, v = phonebook.popitem()
# print(phonebook)
# print(k,':',v, sep='')

# my_values = phonebook.values()
# print(my_values)
#
# for value in my_values:
#     print(value)

# to add a dictionary to a dictionary, or from an iterable we use the dictionary.update()

# d = {1: "one", 2:"three"}
# d1 = {2:"two"}
# d.update(d1) # changes the value of 2 in d dictionary
# print(d)
# d1 = {3:"three"}
# d.update(d1)
# print(d)

# dictionary = {'x':2}
# dictionary.update([('y',3), ('z', 0)])
# print(dictionary)
#
# dict2 = {"Ahmad":122, "Reem":332}
# phonebook.update(dict2)
# print(phonebook)
#
# calling an update function, without passing an arguement, will not change the dictionary
#
# lst = [[1,2],[3,4]]
# phonebook.update(lst)
# print(phonebook)

# upd = [[(1,2),344], [1,5]]
# phonebook.update(upd)
# print(phonebook)
#
# upd = phonebook.update([[('Fajer', 2), [490, 200]]])
# print(phonebook)
# we can use

# Dictionary Exercise

# dictionary = {'Jane':5367, 'John':6254, 'Bob':5689}
# dictionary['Jane'] = 1024
# dictionary.update([('Jane', 3467)])
# dictionary['Anna'] = 3237
# print(dictionary['Bob'])
# print(dictionary.get('Bob'))
#
# print(dictionary.keys())
# print(dictionary.values())


#####################                               Lecture 17 Python                                ######################

# Set: object that stores a collection of data in the same way as a mathematical set

# set1 = {'Sam', 1, 3.5}
# print(type(set1)) # <class 'set'>

# to create an empty set, use set()
# emptSet = set()
# print(emptSet)

# set3 = set(4) # ERROR has to be in an iterable ()
# set4 = set([1,2,4,6])
# set5 = set('Ahmad')
#
# print(set4)
# print(set5)

# my_set = set()
# print(my_set)  # set()
# my_set = set('Hello')
# print(my_set)  # {'o', 'H', 'e', 'l'}
# my_set = set([1, 2, 4, 6, 7, 8, 1])
# print(my_set)  # {1, 2, 4, 6, 7, 8}
# my_set = set((1, 'a', 'July', 7.5))
# print(my_set)  # {'a', 1, 'July', 7.5}


# set methods:

# len(set)  # number of elements in a set

# add  # adds in element to a set
#
# my_set = set()
# my_set.add(5)  # adds 5 to the list
# my_set.add([5])  #error
# print(my_set)
#
# my_set.update([4,[5,6]]) # error, every item in set has to have same level
# print(my_set)

# my_set = set()
# my_set.add(1)
# my_set.add(2)
# my_set.add(3)
# print(my_set)
# my_set.update([4,5,6])
# print(my_set)
# set2 = set([7,8,9,10])
# print(set2)
# my_set.update(set2)
# print(my_set)
# print(set2)
# my_set.update('abcd')
# print(my_set)

# remove an item from set using:
# remove
# discard
# both take the item to be deleted as an argument
# remove raises a keyerror exception if not found
# discard does not raise an exception

# my_set = set('abc')
# my_copy = my_set.copy()
# my_ref_copy = my_set
# my_set.remove('b')
# print(my_set)  # {'c', 'a'}
# print(my_copy) # {'c', 'b', 'a'} # since this is a shallow copy, any change done to original set does not show
# print(my_ref_copy)  #{'c', 'a'}

# a for loop can be used to iterate over a set
# for item in set:
# we can also check if something is in the set
# if 3 in set:
# if 3 not in set:

# we can find the union of two sets using two methods
# set1.union(set2) # returns a new set
# set1 | set2
# all elements in set 1 and set 2 without repeat
# both return a new set, and do not change the original sets

# we can find the union of two sets using two methods
# set1.intersection(set2) # returns a new set
# set1 & set2
# all elements in both set 1 and set 2
# both return a new set, and do not change the original sets

# a = {1, 2, 3, 4}
# b = {3, 4, 2, 7}
# c = {3, 7, 8, 4}
#
# d = a & b & c
# print(d)  # {3, 4}
#
# e = a.intersection(b).intersection(c)
# print(e)  # {3, 4}

# we can find the difference between two sets using two methods
# set1.difference(set2) # returns a new set
# set1 - set2
# all elements in set 1 but not in set 2
# both return a new set, and do not change the original sets

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
#
# set3 = set1.difference(set2)
# set4 = set1 - set2
# set5 = set2.difference(set1)
# set6 = set2 - set1
#
# print(set3)
# print(set4)
# print(set5)
# print(set6)

# Symmetric difference of two sets: a set that contains the elements that are not shared by the two sets كل شي ما عدا التقاطع

# set1 = set([1, 2, 3, 4, 5])
# set2 = set([3, 4, 5, 6, 7])
#
# set3 = set1.symmetric_difference(set2)
# set4 = set1 ^ set2
#
# print(set3)
# print(set4)

# Set A is subset of set B if all the elements in set A are included in set B
# to check use either setA.issubset(setB)
# to check use either setA <= setB

# Set A is superset of set B if it contains all the elements of set B
# to check use either setA.issuperset(setB)
# to check use either setA >= setB

# set1 = set()
# set2 = {4, 5, 6}
# set3 = {4, 5, 6}
# set4 = {4, 5}
# set5 = {7, 8}
# set6 = {7, 8}
#
# print(set1.issubset(set2))  # True
# print(set3.issuperset(set2))  # True
# print(set4 <= set2)  # True
# print(set5 >= set2)  # False
# print(set5.issubset(set6))  # True


# a = {1, 2, 3, 4}
# b = {1, 3, 5, 7}
#
# c = a | b  # a.union(b)
# d = a - b
# e = b.difference(a)  # b - a
# f = a.intersection(b)  # a & b
# g = a ^ b # a.symmetric_difference(b)
#
# print(c)  # {1, 2, 3, 4, 5, 7}
# print(d)  # {2, 4}
# print(e)  # {5, 7}
# print(f)  # {1, 3}
# print(g)  # {2, 4, 5, 7}


#####################                               Lecture 18 Python                                ######################

# What we have done up to this point is all procedural programming

# We'll learn Object oriented programming, where we deal mainly with objects
# that contain data and procedures in a process known as encapsulation

# Advantages of oop: 1- Data hiding 2- Reusability

# Data attributes: defines the state of an object

# to manipulate an object and its attributes from outside, we use public methods

# anything that manipulates attributes without external code is done through private methods

# to define an object in python, we use classes

# classes are basically a user-created type in python

# instances are objects created from a class

# we can think of classes as a blueprint, and of instances as objects built from that blueprint

# First class: Student Class

# Data attributes are also called instance attributes, since they are specific for each instance

# When I create a class, we have to use a constructor to create an instance of that class

# This is done through the initializer method, __init__(self, atr1, atr2..., atrn):
# The initializer is automatically called when a class is called
# Self has to be the first parameter in an initializer
# An initializer is usually the first method in a class definition


# class Student:
#
#     def __init__(self, first='', last='', id=0, gpa=0, credits=0, grades=[]):
#         self.first_name = first
#         self.last_name = last
#         self.id = id
#         self.gpa = gpa
#         self.credits = credits
#         self.grades = grades
#
#     def print_msg(self):
#         # we can create new data attributes inside a method, but it is not recommended
#         print(self.first_name, self.last_name, self.id, self.grades)
#
#     def add_grade(self, g):
#         if g == 'A' or g == 'B' or g == 'C' or g == 'D' or g == 'F':
#             self.grades.append(g)
#             self.credits += 3
#         else:
#             print('Error, Invalid Grade')
#
#
# student1 = Student("Ahmad", "Alqattan", 2192131011, 4.00, 61, ['A'])
# student1.print_msg()
# student1.add_grade('B')
# student1.print_msg()

# import random
#
# class Coin:
#     def __init__(self):
#         self.sideup = 'Heads'
#
#     def toss(self):
#         if random.randint(0,1) == 0:
#             self.sideup = 'Heads'
#         else:
#             self.sideup = 'Tails'
#
#     def get_sideup(self):
#         return self.sideup
#
#
# def main():
#     my_coin = Coin()
#     print('This side is up:', my_coin.get_sideup())
#     print('I am tossing the coin')
#     my_coin.toss()
#     print('This side is up:', my_coin.get_sideup())
#
# main()

# If many instances of a class are created, each would have its own set of attributes

# There are other attributes called class attributes which are shared amongst all instances of that class
# convention is to have them in all upper case

# Although we can use class attributes from class instances,
# we can also use them from class objects, without creating an instance:
# person = Person(a,b,c)
# person.TITLES
# Person.TITLES
