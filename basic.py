def add(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f"sum is {c}")

add(2,4)
add(2,3,4)
add(1,2,3,4,5,6,8)

# add(1,2,'Deepak')

def add(*numbers,name):
    c=0
    print(numbers)
    print(name)
    for i in numbers:
        c+=i
    print(f"Sum is {c}")

add(1,2,name='Jenny')

def add(a,*numbers):
    c=0
    print(numbers)
    for i in numbers:
        c+=i
    print(f"Sum is {c}")

add(1,2,5)


def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

info_person(name='Ram',age=30,dept="cse")
info_person(name="Shyam",dept="Cse")


def info_details(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)

info_details(1,2,3,name='ram',age=20,dept='maths')



"""


def add(a,b):
    c=a+b
    print(f"Sum is {c}")

add(2,3)


def add(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f"sum is {c}")


add(2,3,4)





def greet(name,dept):
    print(f"Hi {name}")
    print(f"Are you from {dept} department")






greet(name='Deepak',dept='Math') # Keyword argument

greet(dept='Maths',name='DeepakDev')

greet('Jenny',dept='cs') # Keyword arguments should be after positional arguments

# greet(dept='Cs','Deepak') # it will through an error since Keyword arguments should be after positional arguments



# Default Arguments 

def greet(name,subject,dept='CS'):
    print(f"Hi {name}")
    print(f"Do you teach {subject}")
    print(f"are you from {dept} department?")



greet("Jenny","python")
greet("Jenny","python",'Maths') # Override the defult value

#SyntaxError: non-default argument follows default argument
# def greet(name,dept='CS',subject):
#     print(f"Hi {name}")
#     print(f"Do you teach {subject}")
#     print(f"are you from {dept} department?")
# greet("Jenny","python")


set1={'Ram','Shyam','Jenny'}
set2={'Jenny','Jiya','Aakash'}
set3={'Ankur','Pradeep'}

print(set1.union(set2))
print(set1.union(set2,set3))
print(set1 | set2 |set3)
print(set1.union('Mohan','Jenny'))
# print(set1 | ('deepak','Ram')) it will through an error
print(set1 | set(('Jeny','Ram')))


set1.update(set2)
set1.update(['Jenny','Mohan'])
set1 |=set3
print(set1)


print(set1.intersection(set2))
print(set1.intersection(set2,set3))
print(set1 & set2)

print(set1.difference(set2))


print(set1-set2)


set2.difference_update(set1)
print(set1)
print(set2)

print(set1.symmetric_difference(set2))

print(set1^set2^set3)

set1.symmetric_difference_update(("Mohan"))
print(set1)
print(set2)



year=int(input("Which year you want to chechk ?"))

if year %4==0:
    if year %100==0:
        if year %400==0:
            print("Leap year")
        else:
            print("No leap year")
    else:
        print("Leap Year")
else:
    print("Not leap yaer")

height=int(input("Enter hieght in feet :"))

if height==3:
    print("Buy Token")
    print("Now you can board the metro")
else:
    print("No token required")

num=int(input("Enter a number "))

if num==1:
    print(1)
elif num==2:
    print(2)
elif num==3:
    print(3)
else:
    print("Wrng Input")
print("Bye")


name="Deepak"
age=27
height=1.6

print(f"My name is {name}. i am {age} years old. My Height is {height} meters")


print(round(21.34567,3))

print(round(21.34567,2))


print(round(21.22))
print(round(674,0))
print(round(674,-1)) # closet multiple of 10
print(round(674,-2)) # closet multiple of 100
print(round(674,-3)) # closet multiple of 1000
print(round(674,2))
print(round(-8/3))
print(round(-8/3,2))
print(round(675,1))

str="asd"
print('a' in str)


print("sa" in str)



a=5
b=5
b='5'
print(a is b)
print(a is not b)
print(a==b)
print(id(a))
print(id(b))



#Bitwise Operator

& and
| or
^ xor
~ Not Complement
<< left Shift
>> Right Shift

a=5 #0101
b=4 #0100
#a&b 0100 -4
#a|b 0101 -5
#a^b 0001 -1
#~a 1010 -10 wrong answer should be -6


print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)


a,b=5,4
print(a>4 and b<19)
print(a>4 and b<2)
print(a>4 or b<19)
a=True
print(not a)



print(len("Deepak"))
print(len("1234"))

# print(len(1234))
length=len("Deepak")

print("Your name has "+str(length)+" Characters")

print(int("10")+int("10"))

print(10+float("10"))

print("Jenn\'s \\n \"Lectures\"")
var=True
print(var,type(var))
var1=0o123
var2=0x123
var3=123
var4=0b101
print(var1,type(var1))
print(var2,type(var2))
print(var3,type(var3))
print(var4,type(var4))
name="Deepak"
print(name[1])
# input("What is your name : ")

# print("Hello "+ input("What is Your namae : "))

a=input("Value 1 ")
b=input("Value 2 ")
temp=a
a=b
b=temp

print("a=  ",a)
print("a=  "+a)

print(type(b))




print("First_program")
print("Print('What to print')")
print("Hell World\n Hello World\n Hello World")
print("Hello"+"Deepak")

def print_hi(name):
    print(f'Hi ,{name}')


if __name__=='__main__':
    print_hi('Pycharm')
    print()
    print_hi('Deepak')

"""
