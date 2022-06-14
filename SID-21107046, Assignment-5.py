# Q1
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
s = "Geeksforgeeks"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string(using loops) is : ",end="")
print (reverse(s))

# Q2
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper):
    if(i%n==0):
        print(i)

# Q3
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)        

# Q4
a='*'
for i in range(1,6):
  print(i*a)
for i in range(4,0,-1):
   print(i*a)



# Q5
n = int(input("Enter number of rows:"))
a=0

for i in range (n):
  for j in range(i+1):
    print(chr(65+a), end="")
    a+=1
  print()
    

# Q6
n=int(input("Enter the number till you want to check: "))
primes = []
for i in range (2, n+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        primes.append(i)
print(primes)

# Q7
nl=[]
for x in range(1,500):
    if (x%7==0) and (x%11==0):
        nl.append(str(x))
print (','.join(nl))


#Q8
# a,b part
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

# c,d part
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# e part
arr=[1,4,5,4,3,3,4,5,6,7]
x=arr.count(1)
y=arr.count(4)
z=arr.count(5)
a=arr.count(3)
b=arr.count(6)
c=arr.count(7)
print("1:",x)
print("4:",y)
print("5",z)   

# Q9
words = ['hello', 'goodbye', 'howdy', 'hello', 'hello', 'hi', 'bye']

print(f'"hello" appears {words.count("hello")} time(s)')
print(f'"howdy" appears {words.count("howdy")} time(s)')

