"""
Task #1
✅ Grade Calculator:
Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F)
 based on the following grading scale:
input-score - 89
output- B
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
If, elif, else
"""

score = int(input("To know your grade, please enter your score between 0 and 100 "))
if score>=0 and score<=59:
    print("You got F Grade");
elif(score>=60 and score<=69):
    print("you got D Grade");
elif(score>=70 and score<=79):
    print("Yout got C Grade");
elif(score>=80 and score<=89):
    print("Yout got C Grade");
elif(score>=90 and score<=100):
    print("Yout got C Grade");
else:
    print("Please enter valid score between 0 and 100");



"""
Task #2
Leap Year Checker:
Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
Input = 2024
Output = Leap year
"""


y = int(input("Please enter the year"))
if(y%4==0 and y%100!=0 or y%400==0):
    print("The year entered is leap year");
else:
    print("The year entered is not leap year");



"""
Task #3
Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is equilateral
(all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
3 Input
side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3
"""


side1 = int(input('Please enter first side of triangle'))
side2 = int(input('Please enter second side of triangle'))
side3 = int(input('Please enter third side of triangle'))
if(side1==side2==side3):
    print('Its an Equilateral triangle')
elif(side1==side2 or side2==side3 or side1==side3):
    print('Its an isosceles triangle')
else:
    print('Its an scalene triange')





