# if-else (voting eligibility)
'''
age = int(input("Enter your age: "))

if age>=18:
    print("You can vote")
else:
    print("You can't vote")
'''

# if-elif-else (traffic light)
'''
light = input("Enter light: ")

if light=="red":
    print("Stop")
elif light=="orange":
    print("Slow down")
elif light=="green":
    print("You can go")
else:
    print("invalid input")
'''

# nested if-else (login validation)
'''
username= input("enter username: ")
password= input("enter password: ")

if username=="admin" and password=="pass":
    print("login successful")
else:
    if(username!="admin"):
        print("incorrect username")
    else:
        print("incorrect password")
'''

# if-else with modulus (divisibility check)
'''
num = int(input("enter num: "))

if num%5 ==0:
    print("divisible")
else:
    print("indivisible")
'''

# even-odd using if-else
'''
num = int(input("enter num: "))

if num%2 ==0:
    print("even")
else:
    print("odd")
'''

# while loop (countdown)
'''
count = 5

while count>=1:
    print(count)
    count=count-1
'''

# while loop (multiplication table)
'''
num = int(input("Enter no:"))

i=1
while i<11:
    print(num*i)
    i=i+1
'''

# continue statement (skip table if number is multiple of 5)
'''
num = int(input("Enter no:"))

i=1
while i<11:
    if(num%5==0):
        i=i+1
        continue
    print(num*i)
    i=i+1
'''

# continue with condition (skip specific multiples in table)
'''
num = int(input("Enter table number: "))
skip = int(input("Enter number to skip its multiples: "))

i = 1
while i <= 10:
    if (num * i) % skip == 0:
        i = i + 1
        continue

    print(num * i)
    i = i + 1
'''

# for loop (character count)
'''
word = "Artificial intelligence"

count = 0

for ch in word:
    if(ch == "i"):
        count+=1

print("count= ", count)
'''

# for loop (vowel count)
'''
word = "artificial intelligence"

vowels = 0

for ch in word:
    if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"):
        vowels+=1

print("vowels = ", vowels)
'''

# for loop (sum of first n numbers)
'''
n = int(input("Enter no: "))

sum=0
for i in range(1, n+1):
    sum+=i
print(sum)
'''

# functions (sum of two numbers)
'''
def sum(a,b):
    s = a+b
    return s 

print(sum(2,3))
'''

# functions (average of three numbers)
'''
def avg(a,b,c):
    a = (a+b+c)/3
    return a

print(avg(2,3,5))
'''

# for loop (factorial program)
'''
num = int(input("Enter number: "))
i = 1

for ch in range(1, num+1):
    num = i*num

print(num)
'''

#Assignment
#1 if-elif-else (salary example)
'''
salary = int(input("Enter salary: "))

if(salary<30000):
    print("5%")
elif(30000<salary<70000):
    print("15%")
else:
    print("25%")
'''
