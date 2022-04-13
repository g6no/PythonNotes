'''
Ahmad Alqattan
2192131011
Homework 1
Question 1
'''

# Question solution #1 using int division and remainder operations
userNum = int(input('Enter a five digit number: '))

# initalize number to be equal
revs_number = 0
# reverse the integer number using the while loop
while userNum > 0:
    remainder = userNum % 10
    revs_number = (revs_number * 10) + remainder
    userNum = userNum // 10

while revs_number > 0:  # while loop iterates till  all digits extracted and prints them
    print(revs_number % 10, end='   ')
    revs_number //= 10
print('\n')

# Question solution #2 using string manipulation
userNum = input('Enter a five digit number: ')

# iterate through each letter in string
for num in userNum:
    print(num, end='   ') # display each letter followed by 3 spaces
print("\n")

# Question Answer: Since both of these solutions don't rely on a count, but rather on the digits of the input itself,
# They can display the correct output format regardless of the number of digits
