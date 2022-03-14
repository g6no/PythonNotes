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
