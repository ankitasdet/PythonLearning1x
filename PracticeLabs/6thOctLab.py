"""
Take a input from a user and print the table
How to use the print with formatting f
print(f''), How can print the same?
n = 2 & print

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
"""

#Solution 1
row1 = "2*1 = {}".format(2*1)
row2 = "2*2 = {}".format(2*2)
row3 = "2*3 = {}".format(2*3)
row4 = "2*4 = {}".format(2*4)
row5 = "2*5 = {}".format(2*5)
row6 = "2*6 = {}".format(2*6)
row7 = "2*7 = {}".format(2*7)
row8 = "2*8 = {}".format(2*8)
row9 = "2*9 = {}".format(2*9)
row10 = "2*10 = {}".format(2*10)

print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
print(row6)
print(row7)
print(row8)
print(row9)
print(row10)


#Solution 2
n = int(input ('Enter the number\n'))
print(f'Table of {n} is :')

print(f'{n} * 1 = {n*1}')
print(f'{n} * 2 = {n*2}')
print(f'{n} * 3 = {n*3}')
print(f'{n} * 4 = {n*4}')
print(f'{n} * 5 = {n*5}')
print(f'{n} * 6 = {n*6}')
print(f'{n} * 7 = {n*7}')
print(f'{n} * 8 = {n*8}')
print(f'{n} * 9 = {n*9}')
print(f'{n} * 10 = {n*10}')








