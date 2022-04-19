'''
Ahmad Alqattan
2192131011
Homework 3
Question 2
'''

message = input('Enter message to encrypt: ')
shift = int(input('Enter amount to shift by: '))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
strng = ''
i = 0

if shift > 26:
    shift = shift - 26

for letter in message.lower():
    if letter in letters:
        index = letters.index(letter)
        if (index + shift) <= len(letters):
            if message[i].islower():
                strng += letters[index + shift]
            else:
                strng += letters[index + shift].upper()
        else:
            if message[i].islower():
                strng += letters[shift - (len(letters) - index)]
            else:
                strng += letters[shift - (len(letters) - index)].upper()
    else:
        # this line to concatenate the spaces and special characters to empty string
        strng += letter
    i += 1

print(strng)
