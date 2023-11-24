"""
27th Oct 2023 Task
### Problem List

1. Write a Python program to find the largest number in a list.

2. Write a Python program to find the smallest number in a list.

3. Write a Python program to sum all numbers in a list.

4. Write a Python program to multiply all numbers in a list.



"""

list1 = [10,20,15,13,18]
# Program 1.  Write a Python program to find the largest number in a list.

print("Largest number in the list is ", max(list1))

# Program 2. Write a Python program to find the smallest number in a list.

print("Smallest number is the list is", min(list1))

# Program 3. Write a Python program to sum all numbers in a list.

print("Sum of all numbers in the list is",sum(list1))


# Program 4. Write a Python program to multiply all numbers in a list.
def multiplyList(list1):
    result = 1
    for i in list1:
        result =result * i
    return(result)
print("Multiplication of all numbers in the list is",multiplyList(list1))


#Program 5: Write a Python program to count the number of strings in a list where the string length is 2 or more
# and the first and last character are the same.
list2= ['Ankita','Kamesh','Karteek']
def filter_list(list2):
    c=0
    for name in list2:
        #print(len(name),name[0],name[-1])
        if len(name)>2 and (name[0].lower() == name[-1].lower()):
            c=c+1
    print("Total Matching strings found in the list are %d"% c)

filter_list(list2)