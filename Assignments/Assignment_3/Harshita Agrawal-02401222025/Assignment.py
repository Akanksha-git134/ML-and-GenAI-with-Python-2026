#1
# Program to print the first 10 natural numbers
def first10():
    for i in range(1,11):
        print(i)

first10()
#2
# Program to calculate the sum of first n natural numbers
def sum(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
n=int(input("Enter a number: "))
print("The sum of the first", n, "natural numbers is:", sum(n))
 
#3
#Program to reverse a number
num=int(input("Enter a number: "))
def reverse(num):
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
print("The reverse of the number is:", reverse(num))

#4
#Program to count the number of digits in a number
num=int(input("Enter a number: "))
def count_digits(num):
    count=0
    while num>0:
        num=num//10
        count+=1
    return count
count=count_digits(num)
print("The number of digits in the number is:", count)

#5
# Program to check if a number is palindrome
num=int(input("Enter a number: "))
def is_palindrome(num):
    rev=0
    temp=num
    while temp>0:
        rem=temp%10
        rev=rev*10+rem
        temp=temp//10
    return rev==num

print("Is the number a palindrome?", is_palindrome(num))

#6
#Program to generate a Fibonacci series up to n terms
n=int(input("Enter the number of terms: "))
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a, end=" ")
        a=b
        b=a+b
fibonacci(n)
print()

#7
#Program to create a calculator
def calculator(operation,num1,num2):
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    elif operation=="/":
        if num2!=0:
            return num1/num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"
operation=input("Enter operation (+, -, *, /): ")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
result=calculator(operation,num1,num2)
print("Result:", result)