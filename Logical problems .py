#  1
num = int(input("enter a number:"))

if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")
else:
    print("odd")

#  2
age = int(input("enter your age:"))

if age  <= 12:
    print("your are child")
elif age >= 13 and age <= 19:
    print("you are teenager")
elif age >= 20 and age <= 39:
    print("you are adult")
elif age >= 40:
    print("you are senior citizen")

#  3
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))

if num1 > num2:
    print(f"{num1} is greater and {num2} is smaller")
elif num1 < num2:
    print(f"{num1} is smaller and {num2} is greater")


#  4
year = int(input("enter a year:"))

if year % 4 == 0:
    print(" year is leap")
else:
    print("year is not leap")


#  5
num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
num3 = int(input("enter a number:"))

maximum = max(num1,num2,num3)
minimum = min(num1,num2,num3)

print(f"maximum number from {num1},{num2}and{num3} is {maximum}")
print(f"minimum number from {num1},{num2}and{num3} is {minimum}")


#  6
exam_score = int(input("enter your exam score:"))

if exam_score >= 90:
    print("your grade is A")
elif exam_score >= 80:
    print("your grade is B")
elif exam_score >= 70:
    print("your grade is C")
elif exam_score >= 60:
    print("your grade is D")
elif exam_score <= 59:
    print("FAil")