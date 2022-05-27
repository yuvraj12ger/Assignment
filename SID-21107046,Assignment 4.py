# Question 1
x=int(input("enter your marks"))
if x>=80:
    print("your grade is 'A'.")
elif x>=60:
     print("your grade is 'B'.")
elif x>=50:
     print("your grade is 'C'.")
elif x>=45:
    print("your grade is 'D'.")
elif x>=25:
    print("your grade is 'E'.")
else:
    print("your grade is 'F'.")

# Question 2
a=int(input("enter the year:"))
if a%400 == 0:
    print(a, "is a leap year.")
elif a%4 == 0:
    print(a, "is aleap year.")
else:
    print(a, "is not aleap year.")                
   

 # Question 3

    import random

    i=0
    while  i<10:
        num1=random.randint(0,10)
        num2=random.randint(0,10)

        print("solve {} * {} =".format(num1,num2))
        ans=int(input("enter your answer :"))

        if ans==num1*num2:
            print("right")
        else:
            print("wrong. The answer is {}".format(num1*num2))
        i+=1

# Question 4
for candies in range(200):
    if candies % 5 == 2:
        if candies % 6 == 3:
            if candies % 7 == 2:
                print(candies, 'candies are in the bowl!')



