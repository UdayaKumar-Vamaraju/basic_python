"""
Problem Explanation:

You are given an array that contains n-1 distinct numbers. These numbers are chosen from the range 1 to n, where 
n is the total number of elements you expect. Since there is one missing number, the array contains every number 
from the range except one.

For example, if n = 6, the complete set of numbers would be: [1, 2, 3, 4, 5, 6]
If the array contains the numbers: [1, 2, 3, 5, 6]
Then the missing number is 4.

"""
n=int(input("Enter the size of an array:"))

arr=[]
print("Enter the numbers:")
for i in range(1,n):
    arr.append(int(input()))

for i in range(1,n):
    if i not in arr:
        print("missing number is:",i)
        break
else:
    print("No number is missing")
