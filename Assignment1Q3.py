'''
Ahmad Alqattan
2192131011
Homework 1
Question 3
'''

# Constant Definition
p = 203e6
r = 0.045

# Variable Definition
num1 = 800e6
n = 0
a = 0

# while loop that checks if the number of users is > number specified
while a < num1:
    n += 1
    a = p * (1 + r)**n
print(f'Snapchat needs {n} months to reach >= {num1/1e6} million users')

# reassigning num1 for use in 2nd while loop
num1 = 1.5e9

#  the value of n and a
n = 0
a = 0

while a < num1:
    n += 1
    a = p*(1 + r) ** n
print(f'Snapchat needs {n} months to reach >= {num1/1e9} billion users')

#extra test

# reassigning num1 for use in 3rd while loop
num1 = 3e9

# resetting the value of n and a
n = 0
a = 0

while a < num1:
    n += 1
    a = p * (1 + r) ** n
print(f'Snapchat needs {n} months to reach >= {num1/1e9} billion users')



