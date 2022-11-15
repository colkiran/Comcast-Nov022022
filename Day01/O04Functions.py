
def greet():
    print("Greetings Mr.Sachin Welcome to the event......")

def greetGst(gname):
    print(f"Greetings Mr.{gname} Welcome to the event......")

# gname is a non default argument, city is a default argument
def greetGstCty(gname, city="Mumbai"):
    print(f"Greeting Mr.{gname} from {city} welcome to the event........")

greet()
print("-" * 40)
greetGst("Sachin")
print("-" * 40)
greetGst("Rahul")
print("-" * 40)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)

def admisn(cname, dob, qlf, gender, conno, adr, city):
    print(f"Name            :{cname}")
    print(f"DOB             :{dob}")
    print(f"Qualification   :{qlf}")
    print(f"Gender          :{gender}")
    print(f"Contact No.     :{conno}")
    print(f"Address         :{adr}")
    print(f"City            :{city}")

# *arg => list, **kwargs => dictionary

admisn("Jack", '21/04/1983', 'B.tech', 'Male', '23554645', 'MG Road, 8th cross', 'Mumbai')

print("-" * 40)
admisn(gender='female', qlf='M.tech', city='Hyderabad', cname='Tina', adr="Gachibowli, 5th main, 2nd cross" , dob="3/09/1982", conno="23423400")

print("-" * 40)
# variable length args

def multiply_all(*numbers):             # more than one argument
    print(numbers)
    print(*numbers)                     # unpack numbers
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = multiply_all(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 40)
def extract_details(**details):
    for k, v in details.items():
        print(k, "=>", v)

extract_details(name="sachin", runs=125, oppn='WestIndies', venue='Sabina Park')

print("-" * 40)

# command line args
import sys

# def add(x, y):
#     return x + y
#
# print(f"The result is :{add(int(sys.argv[1]), int(sys.argv[2]))}")

print("-" * 40)

def Mutiply_me(x, y):
    return x * y

print("The product of %d  and %d is %d" % (30, 40, Mutiply_me(30, 40)))

print("-" * 40)
# supports recursive calls
# factorial of a number and fibanocci series
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

print(f"The factorial of 5 is :{fact(5)}")

print("-" * 40)

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

# iter = int(input("Enter the number of iterations :"))
iter = 7
for i in range(iter):
    print(fibo(i), end=" ")
print()

print("-" * 40)
def arithematic_Calc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithematic_Calc(20, 8)
print(f"res :{res}")

print("-" * 40)
# doc strings
def fun():
    # this is a comment
    "this is a doc string"
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 40)

def fun1(x, y):
    """
    fun1(x, y)
    ----------

    a. if x and y are integers then fun1 returns the sum of the two numbers passed
    b. if x and y are strings the fun1 returns the concatenation of the two strings
    c. if x and y are two different data types then fun1 raises an exception
    """

    return x + y

print(fun1(10, 20))
print(fun1("hello ", "world"))

print("-" * 40)

help(fun1)
