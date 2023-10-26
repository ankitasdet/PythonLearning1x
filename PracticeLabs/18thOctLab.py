"""
TASK1:
 - What is Fibonacci series and Factorial.
 - Take an input and print the series.
ANSWER:
The Fibonacci series is the sequence of numbers (also called Fibonacci numbers),
where every number is the sum of the preceding two numbers, such that the first two terms are '0' and '1'
0+0=0
0+1=1
1+1=2
2+1=3
2+3=5
3+5=8
5+8=13
8+13=21
and so on ...
And it can be written in 2 ways(iterative and recursive)
"""

#Fabonacci Series
n = int(input('please enter how many of Fibonacci series you want to print '))
num1 = 0
num2 = 1
count =0
if n <=0:
    print("Enter positive and valid number")
elif n==1:
    print("The fibonacci series is upto",n,':')
    print(num1)
else:
    print("The fibonacci series of the numbers is:")
    while count<n:
        print(num1)
        nth=num1+num2
        num1=num2
        num2=nth
        count=count+1

#2nd solution of Fibonaci series by using while loop

number=int(input("Enter the number\n"))
a,b = 0,1
while a < number:
    print(a, end='')
    a,b = b, a+b

#Factorial Solution
number = int(input("Enter the number\n"))
if number < 0:
    print("Factorial; is not possible!")
else:
    fact = 1
    for i in range(1,number+1):
        fact = fact*i
print("Fact is ->",fact)
