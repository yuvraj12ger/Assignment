
# Question 1
from calendar import c


str1 = ("Python is a case sensitive language")
print(len(str1))
print(str1[::-1])
print(str1[10::])
print(str1.replace("case sensitive," , "object oriented"))
print(str1.find('a'))
print(str1.replace(" ",""))

# Question 2
Name = input("enter your name")
S_I_D = int(input("enter your sid"))
Department = input("enter your department")
CGPA = float(input("enter your cgpa"))
print("Hey %s, "%Name, "Here!")
print("My SID  is %d" %S_I_D)
print("I am from %s"%Department,"and my CGPA is %f"%CGPA)

# Question 3
a=56
b=10
print(a&b)
print(a|b)
print(a^b)
print("left sift a with 2 bits:",a<<2)
print("left shift b with 2 bits:",b<<2)
print("right shift a with 2 bits:",a>>2)
print("right shift b with 4 bits:",b>>4)

# Question 4
str_2=input("enter a string")
if "name" in str_2:
    print("Yes")
else:
    print("No")




    
    

# Question 5
    x=int(input("First side: "))
    y=int(input("Second side: "))
    z=int(input("Third side: "))
    i=str(bool(x + y > z and y + z > x and x + z > y)).replace(str(True), "Yes").replace(str(False), "No")
    print(i)

    # Question 6
number_1 = int(input("Enter 1st number "))
number_2 = int(input("Enter 2nd number "))
ex_or = number_1 ^ number_2
bin_exor = bin(ex_or)
check_string = str(bin_exor)
a = check_string.count("1")
print(a)