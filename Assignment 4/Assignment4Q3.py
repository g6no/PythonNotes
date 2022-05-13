'''
Ahmad Alqattan
2192131011
Homework 4
Question 2
'''
lst2 = []
for i in range(3):
    print(f'Enter the number of sold items for salesman {i}')
    lst1 = []
    for j in range(5):
        num = int(input(f'Product {j}: '))
        lst1.append(num)
    lst2.append(lst1)
    print()


for i in range(3):
    print(f'Total Number of sold items for salesman {i} is {sum(lst2[i])}')
print()


for i in range(5):
    total = lst2[0][i] + lst2[1][i] + lst2[2][i]
    print(f'Total number of sold items for product {i} is {total}')