'''
age = int(input("Enter your age: "))

if age>=18:
    print("You can vote")
else:
    print("You can't vote")'''

'''
light = input("Enter light: ")

if light=="red":
    print("Stop")
elif light=="orange":
    print("Slow down")
elif light=="green":
    print("You can go")
else:
    print("invalid input")'''

'''
username= input("enter username: ")
password= input("enter password: ")

if username=="admin" and password=="pass":
    print("login successful")
else:
    if(username!="admin"):
        print("incorrect username")
    else:
        print("incorrect password")'''
    

'''
num = int(input("enter num: "))

if num%5 ==0:
    print("divisible")
else:
    print("indivisble")'''
'''
num = int(input("enter num: "))

if num%2 ==0:
    print("even")
else:
    print("odd")'''

'''
count = 5

while count>=1:
    print(count)
    count=count-1'''

'''
num = int(input("Enter no:"))

i=1
while i<11:
    print(num*i)
    i=i+1'''
'''
num = int(input("Enter no:"))

i=1
while i<11:
    if(num%5==0):
        i=i+1
        continue
    print(num*i)
    i=i+1'''

'''
num = int(input("Enter table number: "))
skip = int(input("Enter number to skip its multiples: "))

i = 1
while i <= 10:
    if (num * i) % skip == 0:
        i = i + 1
        continue

    print(num * i)
    i = i + 1'''

'''
word = "Artificial intelligence"

count = 0

for ch in word:
    if(ch == "i"):
        count+=1

print("count= ", count)'''

'''
word = "artificial intelligence"

vowels = 0

for ch in word:
    if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"):
        vowels+=1

print("vowels = ", vowels)'''

'''
n = int(input("Enter no: "))

sum=0
for i in range(1, n+1):
    sum+=i
print(sum)'''

'''
def sum(a,b):
    s = a+b
    return s 

print(sum(2,3))'''

'''
def avg(a,b,c):
    a = (a+b+c)/3
    return a

print(avg(2,3,5))'''

'''
num = int(input("Enter number: "))
i = 1

for ch in range(1, num+1):
    num = i*num
    # i+=1

print(num)'''

#1
'''
salary = int(input("Enter salary: "))

if(salary<30000):
    print("5%")
elif(30000<salary<70000):
    print("15%")
else:
    print("25%")'''

#2






