"""
Task #1
Palindrome Checker:
Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121
Example - pramod
madam - reverse(madam) -> same
Naman -> reverse -> same
Malayalam
Compare String with the Revserse of the string

Task #2
Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
n = 12345
sum = 15
n = 123
sum = 6
"""

# Task1- Palindrome Checker(solution1)
""" 

def reverse_string(input_string):
    reverse_str = ""
    for c in input_string:
        reverse_str =  c +reverse_str
    return reverse_str

original_str = "MADAM"
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
    print("Palindrome")
else:
    print("It is not Palindrome")

#Solution 2

"""
Original_str = "NAMAN"
def is_palindrome(original_str):
    rev_str = original_str[::-1]
    print(rev_str)
    if original_str == rev_str:
        print("Palindrome")
    else:
        print("It is not palindrome")

print(is_palindrome(Original_str))



# Task- 2 Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
# //n = int(input("Please enter the number you want to calculate sum of the digitsx for"))

n = 243
def getSum(n):
    sum=0
    for digit in str(n):
        sum = sum + int(digit)
    return sum

print(getSum(n))