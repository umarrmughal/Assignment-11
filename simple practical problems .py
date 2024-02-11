#  1
price = int(input("enter a price of each item:"))
quantity = int(input("enter a quantity:"))

total_cost = price * quantity

discount_amount = total_cost * (10/100)
discounted_price = total_cost - discount_amount
if total_cost >= 1000:
    print(f"discounted price is {discounted_price}")
else:
    print(f"total cost is {total_cost}")

#  2
temperature = int(input("enter your temperature in ℃:"))

if temperature <= 20:
    print("you should wear a jacket")
else:
    print("no need to wear a jacket")


#  3
side_1 = int(input("enter a side 1:"))
side_2 = int(input("enter a side 2:"))
side_3 = int(input("enter a side 3:"))

if side_1 == side_2 == side_3:
    print("triangle is equilateral")
elif side_1 == side_2 != side_3:
    print("triangle is issosceles")
else:
    print("triangle is scalene")


#  4
pin = 7889
bank_balance = 20000
pincode = int(input("enter pin:"))
amount = int(input("enter amount:"))

if pincode == pin:
    if amount <= bank_balance:
        print("Withdraw your Money")
    else:
        print("insufficent balance")
else:
    print("pin is wrong")

#  5
import calendar

month = int(input("enter a month number (1-12):"))
year = 2024


num_days = calendar.monthrange(year,month)[1]

print(num_days)


#   6
import calendar
month = int(input("enter a month number (1-12):"))
year = int(input("enter a year"))

num_days = calendar.monthrange(year,month)[1]
print(f"{calendar.month_name[month]}-{year} : {num_days}")