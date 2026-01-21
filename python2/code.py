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






