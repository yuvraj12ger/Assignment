# Question 1
a=int(input("enter the no."))
print(a , "in binary is " , bin(a))

# Question 2

# Function to add two numbers 
def add(num1, num2):
    return num1 + num2
  
# Function to subtract two numbers 
def subtract(num1, num2):
    return num1 - num2
  
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
  
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
  
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
  
  
# Take input from the user 
select = int(input("Select operations form 1, 2, 3, 4 :"))
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
  
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
  
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")

    # Question 3
import math
#A)
a = (3+4)*(5)
print("(3+4)*(5)", "=", a)

#B)
a=int(input("Enter the value of 'n' to calculate the value of '(n(n-1))/2': "))
print("For 'n':" , a , ", the value of '(n(n-1))/2' is: " , end="")
print((a*(a-1))/2)

#C)
r=int(input("Enter the value of 'r' to calculate 4pi(r^2): "))
b=4*(math.pi)*(r**2)
print("For 'r':" , r, ", the value of 4pi(r^2) is: " ,end="")
print(f"{b:.4f}")

#D)
A_1=int(input("Value of a in degrees: "))
A_2=int(input("Value of b in degrees: "))
c=A_1*(math.pi)/180
d=A_2*(math.pi)/180
e=int(input("Value of 'r': "))
print("The value of expression '(r*(cos(a)^2) + r*(sin(b)^2))^1/2': " , math.sqrt((e*(math.cos(c))*2) +e*(math.sin(d))**2))

#E)
print("To find the slope between two points.")
X_1=int(input("Enter the point x-axis of point 1: "))
Y_1=int(input("Enter the point y-axis of point 1: "))
X_2=int(input("Enter the point x-axis of point 2: "))
Y_2=int(input("Enter the point y-axis of point 2: "))
print("The slope between 2 points is: " , end="")
print(f"{(Y_2 - Y_1)/(X_2 - X_1):.4f}")

# Question 4
for a in range(5):
    print(a)

for b in range(3,10):
    print(b)
   
for c in range(4,13,3):
    print(c)

for d in range(15,5,-2):
    print(d)

for e in range(5,3,-1):
    print(e)

    # Question 5
H_w = 1.00794
C_w = 12.0107
O_w = 15.9994

H = int(input("Enter number of hydrogen atoms "))
C = int(input("Enter number of carbon atoms "))
O = int(input("Enter number of oxygen atoms "))
         
weight = H*H_w + C*C_w + O*O_w

print("The molecular weight of the compound is", weight)
