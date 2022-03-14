# #Lecture 2 python Dr.Lulwah

print("I'm Ahmad")
print('The book is "starting python"')
print('''I'm Ahmad and I'm using "starting python"''')
print("""I'm Ahmad and I'm using "starting python""")

print("""One
Two
Three""")

# #equivalent statements

print("One")
print("Two")
print("Three")

#equivalent statements

print("One\nTwo\nThree")

'''
This is a comment
Hello
Hi
Heellloooo
Ello
'''


room = 503
print('I am staying in room number', room)
#Items are automatically seperated by a space when displayed on screen


#####################                               Lecture 3 Python                                ######################
dollars = 2.75
print('I have in my account', dollars)
print('I have in my account %s' %dollars) #different ways to print variables in python
print('I have in my account {}'.format(dollars))

# print(type(1)) #<class 'int'>
# print(type(dollars)) #<class 'float'>

# print('Hello', input('Hello'))
firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')

print('Your full name is', firstName, lastName)
print('Your full name is %s %s' %(firstName,lastName))
print('Your full name is {} {}'.format(firstName, lastName))

#input returns a string, to get an int or flot, we wrap the input function with the type function

name = input('What is your name?')
age = int(input('What is your age?'))
income = float(input('What is your income?'))

print(2**3**4)
print((2**3)**4)
print(2**(3**4))

my_num = 5 * 2.0
print(my_num)

f = 2.6
print(int(f))

x = -2.9
print(int(x))

# to break long statements into multiple lines in python
var1 = 1
var2 = 2
var3 = 3
var4 = 4
result = var1 * 2 + var2 * 3 + \
    var3 * 4 + var4 * 5 # example

print(result)
# also, anything inside parentheses can be broken into multiple lines
print("Monday", "Tuesday",
      "Wednesday", "Thursday",
      "Friday")