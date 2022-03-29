'''
Ahmad Alqattan
2192131011
Bonus 3
'''

sum = 0
while True:
    userNum_str = input('Enter a number: ')
    if userNum_str == '.':
        break
    else:
        userNum = int(userNum_str)
        if userNum % 2 == 0:
            sum += userNum
print(sum)