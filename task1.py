# Sum of two numbers

num1  = int(input("enter first number = "))
num2  = int(input("enter second number = "))
sum = num1 + num2
print("Sum = ", sum)


# odd or even checker

num = int(input("enter a number"))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")


#Factorial calculation using loop

num = int(input("enter a number"))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
    
print("factorial = ", fact)


#fibonacci Sequence

n = int(input("How many numbers? "))

x = 0
y = 1

for i in range(n):
    print(x, end=" ")
    z = x + y
    x = y
    y = z

#Reverse string

Company = input("Enter a string: ")

reverse_string = Company[::-1]

print("Reversed String =", reverse_string)


#Palindrome check

#Using String Slicing

Name = input("Enter a name or any string : ")

if Name == Name[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#Leap Year Check

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


#Armstrong number

number = int(input("Enter a number: "))

order = len(str(number))
copy_num = number
sum = 0

while copy_num > 0:
    digit = copy_num % 10
    sum = sum + digit ** order
    temp = copy_num // 10

if number == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")




