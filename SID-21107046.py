# Question 1
num1 = int(input())
num2 = int(input())
num3 = int(input())

avg = (num1+num2+num3)/3
print(avg)

# Question 2
tax_rate=0.20
print("enter your income")
gross_income= int(input())

standard_deduction = 10000

print("enter number of dependents")
dependents = int(input())
dependent_deduction = 3000

taxable_income =gross_income - standard_deduction - (dependents*dependent_deduction)
tax = taxable_income*tax_rate
print(tax)

# Question 3
print("enter number of seconds")
num_sec=int(input())

minutes= int(num_sec//60)
seconds= int(num_sec%60)
print (str(minutes) + " minutes and " + str(seconds)+ " seconds")

# Question 4
num1 = int(25)
num2 = str('25')
num3 = float(25.0)

x = int(num1) + int(num2) + int(num3)
print (str(x))

# Question 5
import math as math

angle = 0
while angle < 360:
    rad = angle * math.pi/180
    print ("angle " + str(angle) + " sin:" + str(round(math.sin(rad),4)) + " cos:" + str(round(math.cos(rad),4)))
    angle = angle + 15

