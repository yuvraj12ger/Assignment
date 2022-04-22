# Question 1
num1 = int(input())
num2 = int(input())
num3 = int(input())

avg = (num1+num2+num3)/3
print(avg)

# Question 2
gross_income=input("please enter gross income: ")
gross_income=float(gross_income)

standard_deduction=10000
dependents=input("enter the no. of dependents: ")
dependents=int(dependents)
#there is a $3000 deduction for each dependents
dependent_deduction=3000

#tax rate=20%
taxable_income=gross_income-standard_deduction-(dependent_deduction*dependents)
tax=(taxable_income*20)/100
print("tax:")
if tax>=0:
    print(tax)
else:
    print("0")


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

